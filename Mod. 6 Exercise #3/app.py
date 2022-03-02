from flask import Flask, render_template, request

app = Flask(__name__) # __name__ refers to the module name

# Navbar template from w3schools.com

@app.route('/home')
def index():
    py_name = request.args.get('queryname')
    return render_template('home.html')

@app.route('/register')
def register():
    py_registers = {}
    py_organizations = ["Let's Code", "History Geeks", "Mathmaticals", "4 Science", "Next Gen Shakespears"]
    register1 = request.form.get('name', 'organization')
    py_registers.append(register1)

    return render_template('registry.html', registers=py_registers)