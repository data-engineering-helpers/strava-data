Knowledge Sharing - Strava data - Retrieve and use
===================================================

# Overview

## References

### Strava API
* [Strava API homepage](https://developers.strava.com/)
* [Strava API - Getting started](https://developers.strava.com/docs/getting-started/)
* [Strava API - Reference guide](https://developers.strava.com/docs/reference/)
  + [Strava API - PolylineMap model](https://developers.strava.com/docs/reference/#api-models-PolylineMap)

### Decode Polylines
* [StackOverflow - Strava API - How to get route image](https://stackoverflow.com/questions/48017792/strava-api-how-to-get-route-image)
* [Google dev - Polyline algorithm](https://developers.google.com/maps/documentation/utilities/polylinealgorithm)
* [Interactive Google utility to decode polylines](https://developers.google.com/maps/documentation/utilities/polylineutility)
* [Mark Needham - Display polylines on Leaflet with Python](https://www.markhneedham.com/blog/2017/04/29/leaflet-strava-polylines-osm/)
* [Mapbox utility in JavaScript](https://github.com/mapbox/polyline)
* [Strava interactive application in React](https://github.com/burger-mtbkr/strava-react-app)
* [StackOverflow - Leaflet application to decode Polylines](https://stackoverflow.com/questions/40694161/decoding-google-maps-api-encoded-overview-polyline-with-javascript-for-use-in-ma/40728445#40728445)

### Leaflet
* Home page: https://leafletjs.com
* [Leaflet - Quick start guide](https://leafletjs.com/examples/quick-start/)
* [GitHub - Leaflet project](https://github.com/Leaflet/Leaflet)

# Quick starter - use cases

## Use Python scripts to retieve trips and display them
* Authenticate with the Strava API as explained in the [Setup section](#setup)
  + Store the access tokem as an environment variable:
```bash
$ export STRAVA_ACCESS_TOKEN="<the-strava-api-access-token>"
```

* Retrieve the trips from Strava into a CSV file (namely
  `data/private/strava-activity-polylines.csv`, which is ignored by GitHub):
```bash
$ python python/strava-leaflet-app/retrieve-strava-activities.py
$ ls -lFh data/private/strava-activity-polylines.csv
-rw-r--r--  1 user group 88K Jul 4 16:44 data/private/strava-activity-polylines.csv
```

* Retrieve the geographical coordinates of the center of the map. For instance,
  open Google Maps (https://maps.google.com) and center it on the area
  where the Strava trips are to be displayed. Copy the geographical coordinates
  (latitude and longitude) from the URL, as on the following screen capture
  ![Google Maps - Copy the geo coordinates](img/google-maps-lil.png)

* Update the coordinates in the
  [`python/strava-leaflet-app/templates/leaflet.html` HTML template file](python/strava-leaflet-app/templates/leaflet.html#19)
  for instance with a text editor

* Launch the Python Flask application to decode and display the polylines on
  an Open Street Map (OSM) Leaflet:
```bash
$ python python/strava-leaflet-app/strava-leaflet-app.py 
 * Serving Flask app 'strava-leaflet-app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5001
Press CTRL+C to quit
```

* Open the browser on http://localhost:5001
  It should display something like
  ![Strava polylines on a Leaflet-powered OSM map](img/strava-polylines-leaflet-osm-lille.png)

## Interact manually with the Strava API with cURL


## Decode a polyline
The quickest to decode a polyline is to go on
[the dedicated Google utility](https://developers.google.com/maps/documentation/utilities/polylineutility)
and:
* Paste the encoded polyline, and/or polyline summary, in the
  "Encoded Polyline" form field at the bottom of the page
* Check the "Unescape special characters in the encoded polylines" box
* Click on the "Decode Polyline" button at the bottom of the page
* Confirm in the dialog box/pop up window

# Setup

## Python environment
* It is recommended to use PyEnv and to install a fairly recent stable Python
  environment (for instance, at the time of writing, Python 3.10.17 or 3.11.4)

* Update the Pip utility, if needed:
```bash
$ python -mpip install -U pip
```

* Install a few Python libraries:
```bash
$ python -mpip install -U flask
```

## Get a Stava API access token
* The access token is valid only for 6 hours, and needs to be refreshed
  every so often

* Get a Strava API authorization code by opening
  open "http://www.strava.com/oauth/authorize?client_id=110070&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=read_all,activity:read_all"
  + Click on the Authorize button
  + In the URL of the just opened page (displaying an error), copy the `code`
    value, it corresponds to the Strava API authorization code

* Use cURL on the command-line to create an access code (and the refresh code):
```bash
$ curl -s -X POST https://www.strava.com/oauth/token -F client_id=<strava-api-client-id> -F client_secret=<strava-api-client-secret> -F code=<strava-api-authorization-code> -F grant_type=authorization_code | jq
```
```javascript

```



