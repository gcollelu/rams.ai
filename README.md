
<h1 align="center">
  <br>
  <a href="#"><img src="https://raw.githubusercontent.com/gcollelu/rams.ai/master/resources/logo.png" alt="RamsAI" width="200"></a>
  <br>
</h1>

<h4 align="center">A creative chef AI able to generate new recipes. 👨‍🍳</h4>

<p align="center">
	<a href="https://forthebadge.com">
      <img src="https://forthebadge.com/images/badges/made-with-python.svg">
    </a>
	<a href="https://forthebadge.com">
      <img src="https://forthebadge.com/images/badges/built-with-love.svg">
	</a>
</p>
<br>
<p align="center">
  <a href="https://saythanks.io/to/gcollelu">
      <img src="https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg">
  </a>
  <a href="https://www.paypal.me/colleluorius">
    <img src="https://img.shields.io/badge/$-donate-ff69b4.svg?maxAge=2592000&amp;style=flat">
  </a>
</p>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#data">Data</a> •
  <a href="#deep-learning">Deep Learning</a> •
  <a href="#credits">Credits</a> •
  <a href="#related">Related</a> •
  <a href="#license">License</a>
</p>


## Key Features

* Generate recipe from specified type of cuisine
* Generate recipe with selected ingredients

## Data

Thanks [Archive.org](https://archive.org/download/recipes-en-201706/) for the data! After a bit of cleaning, here's what our data looks like 

```json
{
   "id":127843,
   "title":"Fruit and Yogurt Treats",
   "ingredients":[
      {
         "amount":"1/3",
         "unit":"cup",
         "name":"SMUCKER'S Strawberry Low Sugar Preserves"
      },
      {
         "amount":"1/4",
         "unit":"cup",
         "name":"JIF Creamy Peanut Butter & Honey"
      },
      {
         "amount":"1",
         "unit":"cup",
         "name":"low-fat vanilla yogurt"
      },
      {
         "amount":"8",
         "unit":null,
         "name":"sugar cones"
      },
      {
         "amount":"4",
         "unit":"cup",
         "name":"fresh mixed fruits: chopped strawberries, bananas, pineapple, mandarin oranges, kiwi and blueberries"
      }
   ],
   "steps":[
      {
         "idx":1,
         "content":"Combine preserves, peanut butter and yogurt until blended."
      },
      {
         "idx":2,
         "content":"Chop fruit small. Place a tablespoon of yogurt mixture into bottom of cone. Fill cone with fruit until heaping. Top fruit with a dollop of yogurt mixture."
      }
   ],
   "rating":3.5
}
```

## Deep Learning

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) and [TensorFlow](https://www.tensorflow.org)

```bash
# Clone this repository
$ git clone https://github.com/gcollelu/rams.ai

```

## Credits

This software uses the following open source packages:

- [TensorFlow](https://www.tensorflow.org)
- [MIT](https://web.mit.edu/)
- [Trello](http://showdownjs.github.io/showdown/)



