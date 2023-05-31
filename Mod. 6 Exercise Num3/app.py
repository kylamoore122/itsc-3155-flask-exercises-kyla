from flask import Flask, render_template, request

app = Flask(__name__) # __name__ refers to the module name

# Navbar template from w3schools.com

@app.route('/')
def index():
    py_name = request.args.get('queryname')
    return render_template('home.html')

@app.get('/registry')
def registery():
    register()
    return "0"

@app.post('/registry')
def register():
    py_registers = {}
    py_organizations = ["Let's Code", "History Geeks", "Mathmaticals", "4 Science", "Next Gen Shakespears"]
    registerN, registerO = request.form.get('name'), request.form.get('organization')
    py_registers[registerN] = registerO

    return render_template('registry.html', registers=py_registers)