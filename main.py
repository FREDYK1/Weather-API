from flask import Flask, render_template
import pandas as pd


page = Flask(__name__)

station_table_df = pd.read_csv("data_small/stations.txt", skiprows=17)
station_table = station_table_df[["STAID", "STANAME                                 "]]

@page.route("/")
def home():
    return render_template("home.html" ,table=station_table.to_html())

@page.route("/api/<station>/<date>")
def temp(station, date):
    df = pd.read_csv("data_small/TG_STAID" + str(station).zfill(6) + ".txt", skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
    return {
        "station": station,
        "date": date,
        "temperature": temperature
    }

@page.route("/api/<station>")
def station_hist(station):
    station_hist_df= pd.read_csv("data_small/TG_STAID" + str(station).zfill(6) + ".txt", skiprows=20,
                                 parse_dates=["    DATE"])
    return render_template("station_hist.html" ,table=station_hist_df.to_html(),
                           station="Station " + station, title="Station " + station + " Weather History")

@page.route("/api/yearly/<station>/<year>")
def station_yearly_hist(station, year):
    station_hist_df= pd.read_csv("data_small/TG_STAID" + str(station).zfill(6) + ".txt", skiprows=20)
    station_hist_df["    DATE"] = station_hist_df["    DATE"].astype(str)
    station_hist_df = station_hist_df[station_hist_df["    DATE"].str.startswith(str(year))]
    return render_template("station_yearly_hist.html" ,table=station_hist_df.to_html(),
                           station="Station " + station, title="Station " + station + " ("+ year.split("-")[0] +
                                                               " Weather History)")



if __name__ == "__main__":
    page.run(debug=True)