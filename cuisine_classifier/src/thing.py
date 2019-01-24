import os
import numpy as np 
import pandas as pd 
from pandas import read_csv

print(os.listdir("../data"))
pd.set_option('display.max_colwidth', -1)
np.random.seed(7)

train_filename =  '../data/train.json'
test_filename =  '../data/test.json'

def flatten_json(input_file):
    import json
    import re
    from pandas.io.json import json_normalize
    corpus_file = open(input_file,"r")
    corpus = corpus_file.read()
    entries =  json.loads(corpus)
    df =  json_normalize(entries)
    df['flat_ingredients'] = df.apply(lambda row: ' '.join(ingredient for ingredient in row['ingredients']), axis=1)
    df['word_count'] = df.apply(lambda row: len(row['flat_ingredients'].split(' ')), axis=1)
    df.drop('ingredients', axis=1, inplace=True)   
    df.sort_values(['word_count'], ascending=False, inplace=True)
    return df                          
        
train_data_raw = flatten_json(train_filename)
test_data_raw = flatten_json(test_filename)

train_data_raw.head()


from keras.preprocessing import text, sequence
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

vocab_size =  50000            # based on words in the entire corpus
max_len = 64                   # based on word count in phrases

all_corpus     = list(train_data_raw['flat_ingredients'].values) + list(test_data_raw['flat_ingredients'].values)
train_phrases  = list(train_data_raw['flat_ingredients'].values) 
test_phrases   = list(test_data_raw['flat_ingredients'].values)
X_train_target_binary = pd.get_dummies(train_data_raw['cuisine'])
columns = X_train_target_binary.columns.tolist()

#Vocabulary-Indexing of the train and test flat_ingredients, make sure "filters" parm doesn't clean out punctuations
tokenizer = Tokenizer(num_words=vocab_size)
tokenizer.fit_on_texts(all_corpus)
word_index = tokenizer.word_index
print("word_index", len(word_index))

encoded_train_phrases = tokenizer.texts_to_sequences(train_phrases)
encoded_test_phrases = tokenizer.texts_to_sequences(test_phrases)

#Watch for a POST padding, as opposed to the default PRE padding
X_train_words = sequence.pad_sequences(encoded_train_phrases, maxlen=max_len,  padding='post')
X_test_words = sequence.pad_sequences(encoded_test_phrases, maxlen=max_len,  padding='post')
print (X_train_words.shape)
print (X_test_words.shape)
print (X_train_target_binary.shape)

X_train_num = train_data_raw['word_count']
X_test_num = test_data_raw['word_count']

print ('Done Tokenizing and indexing phrases based on the vocabulary learned from the entire Train and Test corpus')


from keras.callbacks import EarlyStopping
from keras.layers import Dense, Input, LSTM, Embedding, Dropout, Activation, Conv1D, CuDNNGRU, CuDNNLSTM, BatchNormalization
from keras.layers import  GlobalMaxPool1D, SpatialDropout1D
from keras.layers import Bidirectional
from keras.models import Model
from keras.layers.merge import concatenate

early_stop = EarlyStopping(monitor = "val_loss", mode="min", patience = 3, verbose=1)

print("Building layers")        
nb_epoch = 10
print('starting to stitch and compile  model')
from keras.initializers import he_normal
initializer = he_normal(seed=None)

input_numeric = Input((1, ))
dense_num = Dense(32, activation='relu')(input_numeric)

# Embedding layer for text inputs
input_words = Input((max_len, ))
x_words = Embedding(vocab_size, 300, input_length=max_len)(input_words)
x_words = Bidirectional(CuDNNLSTM(50, return_sequences=True))(x_words)
x_words = Dropout(0.5)(x_words)
x_words = Conv1D(64, 3,   activation='relu')(x_words)
x_words = Conv1D(64, 1,   activation='relu')(x_words)
x_words = GlobalMaxPool1D()(x_words)
x_words = Dropout(0.5)(x_words)

# merge
merged = concatenate([x_words, dense_num])
x = Dense(64, activation="relu")(merged)
predictions = Dense(20, activation="softmax")(x)

model = Model(inputs=[input_words, input_numeric], outputs=predictions)
model.compile(optimizer='nadam',loss='categorical_crossentropy', metrics=['accuracy'])
print(model.summary())


#fit the model
history = model.fit([X_train_words, X_train_num], X_train_target_binary, epochs=nb_epoch, verbose=1, batch_size = 128, callbacks=[early_stop], validation_split = 0.2, shuffle=True)
train_loss = np.mean(history.history['loss'])
val_loss = np.mean(history.history['val_loss'])
print('Train loss: %f' % (train_loss))
print('Validation loss: %f' % (val_loss))


pred = model.predict([X_test_words,X_test_num], batch_size=128, verbose = 1)
print (pred.shape) 
max_pred = np.round(np.argmax(pred, axis=1)).astype(int)
cuisines = [columns[m] for m in max_pred]
df =pd.DataFrame({'cuisines': cuisines}).reset_index()
df.groupby('cuisines').agg('count')
submission = pd.DataFrame({'id':test_data_raw['id'],'cuisine': cuisines})
submission.to_csv('submission.csv',index=False)