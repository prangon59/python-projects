from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

station_details = pd.read_csv("data-small/stations.txt", skiprows=17)
station_details = station_details[["STAID", "STANAME                                 "]] # Only shows these 2 columns and the whitespaces on staname are from the stations.txt file

@app.route("/")
def home():
    return render_template("home.html", data = station_details.to_html())

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = f"data-small\TG_STAID{str(station).zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10 

    return {"station": station,
            "date": date,
            "temperature": temperature
            }

@app.route("/api/v1/<station>")
def station_data(station):
    filename = f"data-small\TG_STAID{str(station).zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(orient="records")
    return result

@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station, year):
    filename = f"data-small\TG_STAID{str(station).zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    return result

if __name__ == "__main__":
    app.run(debug=True)