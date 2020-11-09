from flask import Flask, render_template, request, redirect, url_for
from joblib import load
from get_tweets import get_related_tweets

pipeline = load("text_classification.joblib")


def requestResults(name):
    tweets = get_related_tweets(name)
    tweets['prediction'] = pipeline.predict(tweets['tweet_text'])
    ## data = str(tweets.prediciton.value_counts()) + '\n\n'

    return str(tweets)


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        user = request.form['search']
        return "<xmp>" + str(requestResults(user)) + " </xmp> "


@app.route('/success/<name>')
def success(name):
    return ""


if __name__ == '__main__':
    app.run(debug=True)
