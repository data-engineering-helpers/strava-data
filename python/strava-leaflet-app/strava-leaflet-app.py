#
# File: https://github.com/data-engineering-helpers/strava-data/blob/main/python/strava-leaflet-app/strava-leaflet-app.py
# Inspired by https://www.markhneedham.com/blog/2017/04/29/leaflet-strava-polylines-osm/
#
from flask import Flask
from flask import render_template
import csv
import json

app = Flask(__name__)

@app.route('/')
def my_runs():
    runs = []
    with open("data/private/strava-activity-polylines.csv", "r") as runs_file:
        reader = csv.DictReader(runs_file)

        for row in reader:
            runs.append(row["polyline"])

    return render_template("leaflet.html", runs = json.dumps(runs))

if __name__ == "__main__":
    app.run(port = 5001)
