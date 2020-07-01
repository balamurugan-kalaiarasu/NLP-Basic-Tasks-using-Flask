from flask import Flask, render_template, url_for, request
import NLP

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test', methods = ['POST'])
def test():
    text = request.form['message']
    if 'tok' in request.form:
        result = NLP.get_tokens(text)
        return render_template('index.html', result_text = result)
    if 'pos' in request.form:
        result = NLP.get_pos_tags(text)
        return render_template('index.html', result_text = result)
    if 'sen' in request.form:
        result = NLP.get_sentiment(text)
        return render_template('index.html', result_text = result)
    if 'ent' in request.form:
        result = NLP.get_entities(text)
        return render_template('index.html', result_text = result)

if __name__ == '__main__':
    app.run(debug = True)