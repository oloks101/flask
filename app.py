from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, It's Monday and I'm tired as usual!"