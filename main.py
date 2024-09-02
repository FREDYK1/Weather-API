from flask import Flask, render_template

page = Flask(__name__)

@page.route("/")
def home():
    return render_template("home.html")

@page.route("/api/<station>/<date>")
def temp(station, date):
    temperature = 23
    return {
        "station": station,
        "date": date,
        "temperature": temperature
    }


if __name__ == "__main__":
    page.run(debug=True)