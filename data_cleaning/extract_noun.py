
import nltk
# nltk.download('brown')
# nltk.download('punkt')
lines = 'diced rhubarb'
# function to test if something is a noun

# do the nlp stuff
nouns = [word for (word, pos) in nltk.pos_tag(nltk.word_tokenize(lines)) if (lambda pos: pos[:2] == 'NN')] 
nouns
print(nouns)