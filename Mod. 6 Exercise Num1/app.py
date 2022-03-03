from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__) # __name__ refers to the module name

@app.route('/')
def index():
    py_date = str(datetime.now())
    return render_template('index.html', date=py_date)