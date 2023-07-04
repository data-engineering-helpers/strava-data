#
# File: https://github.com/data-engineering-helpers/strava-data/blob/main/python/strava-leaflet-app/retrieve-strava-activities.py
# Inspired by https://www.markhneedham.com/blog/2017/04/29/leaflet-strava-polylines-osm/
#
import requests
import os
import sys
import csv

token = os.environ["STRAVA_ACCESS_TOKEN"]
headers = {'Authorization': "Bearer {0}".format(token)}

with open("data/private/strava-activity-polylines.csv", "w") as runs_file:
    writer = csv.writer(runs_file, delimiter=",")
    writer.writerow(["id", "polyline"])

    page = 1
    while True:
        r = requests.get("https://www.strava.com/api/v3/athlete/activities?page={0}".format(page), headers = headers)
        response = r.json()

        if len(response) == 0:
            break
        else:
            for activity in response:
                r = requests.get("https://www.strava.com/api/v3/activities/{0}?include_all_efforts=true".format(activity["id"]), headers = headers)
                polyline = r.json()["map"]["polyline"]
                writer.writerow([activity["id"], polyline])
            page += 1
