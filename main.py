from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello</h1>'
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#Creating telegtambot.herokuapp.com... done
#HEROKU_OAUTH_ID=09eb2f3e-c3b4-4db6-974c-395cb83b6c5f
#HEROKU_OAUTH_SECRET=5b2c10e6-5e7c-4b3c-8607-71282a5c298d


#heroku config:set -a telegtambot HEROKU_OAUTH_ID=09eb2f3e-c3b4-4db6-974c-395cb83b6c5f HEROKU_OAUTH_SECRET=5b2c10e6-5e7c-4b3c-8607-71282a5c298d
