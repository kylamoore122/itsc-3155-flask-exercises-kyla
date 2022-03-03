from flask import Flask, render_template, request

app = Flask(__name__) # __name__ refers to the module name

@app.route('/')
def index():
    py_name = request.args.get('queryname')
    return render_template('home.html', name=py_name)

@app.post('/submit')
def submit():
    py_integer = request.form.get('integer')
    py_phrase = ""

    print("[Try block attempted]")
    if py_integer.isnumeric():
        print("Integer found!")
        if int(py_integer) % 2 == 0:
            py_phrase = str(py_integer) + " is even"
            print("Integer is even!")
        else:
            py_phrase = str(py_integer) + " is odd"
            print("Integer is odd!")
    elif str(py_integer) == "":
        py_phrase = "No number provided!"
        print("No text provided!")
    else:
        py_phrase = str(py_integer) + " is not an integer!"
        print("Non-integer found!")

    return render_template('submit.html', phrase=py_phrase)