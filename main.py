from flask import Flask, render_template
import pandas as pd


page = Flask(__name__)


@page.route("/")
def home():
    return render_template("home.html")

@page.route("/api/<station>/<date>")
def temp(station, date):
    df = pd.read_csv("data_small/TG_STAID" + str(station).zfill(6) + ".txt", skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
    return {
        "station": station,
        "date": date,
        "temperature": temperature
    }


if __name__ == "__main__":
    page.run(debug=True)