from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route('/about')
def about_page():
    return "<p>This is a about page</p>"