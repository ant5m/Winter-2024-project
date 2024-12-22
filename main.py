from flask import Flask, render_template, request
from spoti import *
from waitress import serve
app = Flask(__name__)

@app.route('/')
@app.route('/home')   #routes to home
def home():
    return "Hi"

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port = 8000) #runs on local port