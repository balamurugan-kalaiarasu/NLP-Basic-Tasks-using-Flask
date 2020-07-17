# NLP Basic Tasks - using Flask
![lang](https://img.shields.io/badge/python-v3.7-blue)
![lang](https://img.shields.io/badge/Tech-Flask%2C%20Textblob%2C%20Spacy%2C%20Vader-green)

Deployed in https://nlp-basic-tasks-using-flask.herokuapp.com/

This is a Flask application with basic tasks in NLP. This is to understand what the below concepts are.

NLP Tasks:
* Tokenization
* POS-Tags
* Entities
* Sentiment Analysis
  * TextBlob Sentiment Analysis
  * Vader Sentiment Analysis
 

### Tokenization
Tokenization refers to dividing text or a sentence into a sequence of tokens, which roughly correspond to “words” using TextBlob package. This is one of the basic tasks of NLP.

### POS-Tags
Part-of-speech(POS) tagging or grammatical tagging is a method to mark words present in a text on the basis of its definition and context. In simple words, it tells whether a word is a noun, or an adjective, or a verb, etc. 

### Entity Extraction
Named entity recognition is a sub-task of information extraction that seeks out and categorises specified entities in a body or bodies of texts.

### Sentiment Analysis
Sentiment analysis is basically the process of determining the attitude or the emotion of the writer, i.e., whether it is positive or negative or neutral.

**Textblob** package returns two properties, polarity and subjectivity. Polarity is float which lies in the range of [-1,1] where 1 means positive statement and -1 means a negative statement. The subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective.

**VADER** (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media. The Positive, Negative and Neutral scores represent the proportion of text that falls in these categories. This means our sentence was rated as 67% Positive, 33% Neutral and 0% Negative. Hence all these should add up to 1. The Compound score is a metric that calculates the sum of all the lexicon ratings which have been normalized between -1(most extreme negative) and +1 (most extreme positive). 

#### Screenshots
