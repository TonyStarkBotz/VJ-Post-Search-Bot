# Don't Remove Credit @TonyStark_Botz
# Join our Telegram Channel For Amazing Bot @TonyStark_Botz
# Ask Doubt on telegram @TonyStarkBotzXSupport

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'TonyStark'


if __name__ == "__main__":
    app.run()
