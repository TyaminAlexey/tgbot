from flask import Flask, request, jsonify
import json
import urllib
import nltk
import random
import requests
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
app = Flask(__name__)




@app.route('/post/', methods=['GET', 'POST'])
def json_example():

    req = request.get_json()
    reqjson = req['text']


    return {
        'text': reqjson
    }, 200

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=8090)
