from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, It's Tuesday and I'm still tired as usual!"