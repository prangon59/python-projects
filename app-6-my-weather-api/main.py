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

if __name__ == "__main__":
    app.run(debug=True)