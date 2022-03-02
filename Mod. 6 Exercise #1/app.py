from flask import Flask, render_template, request

app = Flask(__name__) # __name__ refers to the module name

@app.route('/')
def index():
    py_date = request.args.get('date')
    py_time = request.args.get('time')
    return render_template('index.html', date=py_date, time=py_time)