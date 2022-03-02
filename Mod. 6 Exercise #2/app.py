from flask import Flask, render_template, request

app = Flask(__name__) # __name__ refers to the module name

@app.route('/home')
def index():
    py_name = request.args.get('queryname')
    return render_template('home.html', name=py_name)

@app.route('/submit')
def submit():
    py_integer = request.args.get('integer')
    py_phrase = ""

    if int(py_integer) == int:
        if int(py_integer) % 2 == 0:
            py_phrase = str(py_integer) + " is even"
        else:
            py_phrase = str(py_integer) + " is odd"
    elif str(py_integer) == "":
        py_phrase = "No number provided!"
    else:
        py_phrase = str(py_integer) + " is not an integer!"

    return render_template('submit.html', phrase=py_phrase)