from textblob import TextBlob
import spacy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

nlp = spacy.load('en_core_web_sm')

# Methods
def get_tokens(text):
	raw_text = str(text)
	new_text = TextBlob(raw_text)
	final_text = list(str(new_text.words).split(" "))
	result = '\nTokens:{}'.format(final_text)
	return result

def get_pos_tags(text):
	raw_text = str(text)
	new_text = TextBlob(raw_text)
	final_text = new_text.tags
	result = '\nPOS of Speech : {}'.format(final_text)
	return result

def get_entities(text):
	raw_text = str(text)
	docx = nlp(raw_text)
	final_text = [(entity.text,entity.label_) for entity in docx.ents ]
	result = '\nEntities:{}'.format(final_text)
	return result

def get_sentiment(text):
    raw_text = str(text)
    new_text = TextBlob(raw_text)
    sub = round(new_text.sentiment.subjectivity, 2)
    pol = round(new_text.sentiment.polarity, 2)
    result = '\nSubjectivity: {}, \nPolarity: {}'.format(sub, pol)
    return result

def get_vader_sentiment(text):
    raw_text = str(text)
    analyser = SentimentIntensityAnalyzer()
    score = analyser.polarity_scores(raw_text)
    result = '\nPositive: {}, \nNegativity: {}, \nNeutral: {}, \nCompound: {}'.format(round(score['pos'], 2), 
                                                                                 round(score['neg'], 2),
                                                                                 round(score['neu'], 2),
                                                                                 round(score['compound'], 2))
    textblob_sentiment = get_sentiment(text)
    final_result = '\nTextBlob Sentiment:' + textblob_sentiment + '\n\nVader Sentiment:' + result
    return final_result

#print(get_vader_sentiment('The intent behind the movie was great, but it could have been better'))
