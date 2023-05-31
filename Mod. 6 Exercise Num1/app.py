from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__) # __name__ refers to the module name

@app.route('/')
def index():
    py_date = str(datetime.now())
    py_weekday = datetime.now().isoweekday()
    py_day = str(datetime.now().day)
    py_month = datetime.now().strftime("%B")
    py_year = str(datetime.now().year)
    py_hour = str(datetime.now().hour)
    py_minute = str(datetime.now().minute)
    py_second = str(datetime.now().second)

    if (py_weekday == 1):
        py_weekday = "Monday"
    elif (py_weekday == 2):
        py_weekday = "Tuesday"
    elif (py_weekday == 3):
        py_weekday = "Wedneday"
    elif (py_weekday == 4):
        py_weekday = "Thursday"
    elif (py_weekday == 5):
        py_weekday = "Friday"
    elif (py_weekday == 6):
        py_weekday = "Saturday"
    elif (py_weekday == 7):
        py_weekday = "Sunday"

    return render_template('index.html', date=py_date, weekday=py_weekday, day=py_day, month=py_month, year=py_year, hour=py_hour, minute=py_minute, second=py_second)