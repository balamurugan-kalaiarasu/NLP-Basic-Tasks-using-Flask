from textblob import TextBlob
import spacy
nlp = spacy.load('en')

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
    result = '\nSubjectivity:{}, Polarity:{}'.format(sub, pol)
    return result
