from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

def analysis_tweet(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'positive talk', "😊"
    elif analysis.sentiment.polarity < 0:
        return 'negative talk', "☹"
    else:
        return 'nutral talk', "🙂"

@app.route('/')
def admin():
    return render_template('index.html')

@app.route('/admin', methods=['POST'])
def analz():
    if request.method == 'POST':
        text = request.form['text']
        sentiment, emoji = analysis_tweet(text)
        return render_template('admin.html', mytext=text, mysentiment=sentiment, myemoji=emoji)
    
    return "Invalid request"

if __name__ == '__main__':
    app.debug = True
    app.run()