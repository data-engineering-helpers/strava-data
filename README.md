Knowledge Sharing - Strava data - Retrieve and use
===================================================

# Table of Content (ToC)
* [Knowledge Sharing \- Strava data \- Retrieve and use](#knowledge-sharing---strava-data---retrieve-and-use)
* [Table of Content (ToC)](#table-of-content-toc)
* [Overview](#overview)
* [References](#references)
  * [Jupyter amd Spark](#jupyter-amd-spark)
    * [Spark](#spark)
  * [Spark Connect](#spark-connect)
    * [Jupyter](#jupyter)
  * [Strava API](#strava-api)
    * [Authentication \- OAuth](#authentication---oauth)
  * [Decode Polylines](#decode-polylines)
  * [Leaflet](#leaflet)
    * [Leaflet in Jupyter](#leaflet-in-jupyter)
  * [Build an application with Vue and FastAPI](#build-an-application-with-vue-and-fastapi)
* [Quick starter](#quick-starter)
  * [Launch Jupyter with a PySpark/Spark Connect client kernel](#launch-jupyter-with-a-pysparkspark-connect-client-kernel)
* [Use cases](#use-cases)
  * [Use Jupyter Lab to retrieve trips and display them](#use-jupyter-lab-to-retrieve-trips-and-display-them)
  * [Use Python scripts to retrieve trips and display them](#use-python-scripts-to-retrieve-trips-and-display-them)
  * [Interact manually with the Strava API with cURL](#interact-manually-with-the-strava-api-with-curl)
    * [Retrieve a few details from the Strava profile](#retrieve-a-few-details-from-the-strava-profile)
    * [Retrieve the list of activities/trips](#retrieve-the-list-of-activitiestrips)
    * [Retrieve the details for a specific activity](#retrieve-the-details-for-a-specific-activity)
  * [Decode a polyline](#decode-a-polyline)
* [Setup](#setup)
  * [Python environment](#python-environment)
  * [Create an application for Strava API](#create-an-application-for-strava-api)
  * [Authorize the application to use Strava API](#authorize-the-application-to-use-strava-api)
    * [Generate an authorization code with the internet browser](#generate-an-authorization-code-with-the-internet-browser)
  * [Generate an access token](#generate-an-access-token)
    * [Generate the access and refresh tokens with the CLI](#generate-the-access-and-refresh-tokens-with-the-cli)
      * [Store the access and refresh tokens as environment variables](#store-the-access-and-refresh-tokens-as-environment-variables)
    * [Refresh the access and refresh tokens with the CLI](#refresh-the-access-and-refresh-tokens-with-the-cli)
      * [Store the access token as environment variable](#store-the-access-token-as-environment-variable)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)


# Overview
[This project](https://github.com/data-engineering-helpers/strava-data)
intends to document requirements and referential material to implement
data-driven applications on top of Strava data.

Even though the members of the GitHub organization may be employed by
some companies, they speak on their personal behalf and do not represent
these companies.

# References

## Jupyter amd Spark
The
[DataBricks examples project on GitHub](https://github.com/data-engineering-helpers/databricks-examples)
explains how to setup PySpark and Jupyter Lab so that Jupyter notebooks use
[Spark Connect](https://spark.apache.org/docs/latest/spark-connect-overview.html):
* [GitHub - DataBricks examples - ](https://github.com/data-engineering-helpers/databricks-examples/blob/main/README.md#initial-setup)
* Most of the Jupyter notebook examples in this project make use of
  Spark Connect. Refer to the above-mentioned project to setup Jupyter, Spark
  and Spark Connect properly

### Spark
* [Apache Spark - Download Spark manually](https://spark.apache.org/docs/latest/api/python/getting_started/install.html#manually-downloading)
* [Apache Spark - Doc - Getting started / Installation](https://spark.apache.org/docs/latest/api/python/getting_started/install.html)

## Spark Connect
* [Apache Spark - Doc - Spark Connect - Overview](https://spark.apache.org/docs/latest/spark-connect-overview.html)
* [Apache Spark - Doc - Spark Connect - Quick start](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_connect.html)
* [GitHub - Data Engineering Helpers - Example of Jupyter notebook using Spark Connect](https://github.com/data-engineering-helpers/databricks-examples/blob/main/ipython-notebooks/simple-connect.ipynb)

### Jupyter
* [BMC - Integrate PySpark with Jupyter](https://www.bmc.com/blogs/jupyter-notebooks-apache-spark/)

## Strava API
* [Strava API homepage](https://developers.strava.com/)
* [Strava API - Getting started](https://developers.strava.com/docs/getting-started/)
* [Strava API - Reference guide](https://developers.strava.com/docs/reference/)
  + [Strava API - PolylineMap model](https://developers.strava.com/docs/reference/#api-models-PolylineMap)

### Authentication - OAuth
* [Observable HQ - OAuth 2.0 client examples - Strava](https://observablehq.com/@tomlarkworthy/oauth-examples#strava)
* [Auth0 - OAuth 2.0 Authorization framework](https://auth0.com/docs/authenticate/protocols/oauth)

## Decode Polylines
* [StackOverflow - Strava API - How to get route image](https://stackoverflow.com/questions/48017792/strava-api-how-to-get-route-image)
* [Google dev - Polyline algorithm](https://developers.google.com/maps/documentation/utilities/polylinealgorithm)
* [Interactive Google utility to decode polylines](https://developers.google.com/maps/documentation/utilities/polylineutility)
* [Mark Needham - Display polylines on Leaflet with Python](https://www.markhneedham.com/blog/2017/04/29/leaflet-strava-polylines-osm/)
* [Mapbox utility in JavaScript](https://github.com/mapbox/polyline)
* [Strava interactive application in React](https://github.com/burger-mtbkr/strava-react-app)
* [StackOverflow - Leaflet application to decode Polylines](https://stackoverflow.com/questions/40694161/decoding-google-maps-api-encoded-overview-polyline-with-javascript-for-use-in-ma/40728445#40728445)

## Leaflet
* Home page: https://leafletjs.com
* [Leaflet - Quick start guide](https://leafletjs.com/examples/quick-start/)
* [GitHub - Leaflet project](https://github.com/Leaflet/Leaflet)

### Leaflet in Jupyter
* [GitHub - Folium](https://github.com/python-visualization/folium)
* [GitHub - iPyLeaflet](https://github.com/jupyter-widgets/ipyleaflet)
  + [ReadTheDocs - iPyLeaflet](https://ipyleaflet.readthedocs.io/en/latest/index.html)

## Build an application with Vue and FastAPI
* [StackOverflow - How to connect VueJS and FastAPI](https://stackoverflow.com/questions/64522736/how-to-connect-vue-js-as-frontend-and-fastapi-as-backend)
* [GitHub - TestDriven.io - Developing a Single Page App with FastAPI and Vue.js](https://github.com/testdrivenio/fastapi-vue/tree/main)
* [Medium - How to Create a web app using FastAPI, Vuejs and MongoDB for generating and showcasing images generated by Stability AI API](https://medium.com/@sangeeth123sj/how-to-create-a-web-app-using-fastapi-vuejs-and-mongodb-for-generating-and-showcasing-images-193ccdb20091)
* [Auth0 - Hello World Full-Stack Security:
Vue.js v2/JavaScript + FastAPI/Python](https://developer.auth0.com/resources/code-samples/full-stack/hello-world/basic-access-control/spa/vue-v2-javascript/fastapi-python)

# Quick starter

## Launch Jupyter with a PySpark/Spark Connect client kernel
* From a dedicated terminal window/tab, launch Spark Connect server.
  Note that the `SPARK_REMOTE` environment variable should not be set at this
  stage, otherwise the Spark Connect server will try to connect to the
  corresponding Spark Connect server and will therefore not start
```bash
$ sparkconnectstart
```

* From the current terminal/tab, different from the window/tab having launched
  the Spark Connect server, launch PySpark from the command-line, which in
  turn launches Jupyter Lab
  + Follow the details given by PySpark to open Jupyter in a web browser
```bash
$ export SPARK_REMOTE="sc://localhost:15002"; pyspark
...
[C 2023-06-27 21:54:04.720 ServerApp] 
    
    To access the server, open this file in a browser:
        file://$HOME/Library/Jupyter/runtime/jpserver-21219-open.html
    Or copy and paste one of these URLs:
        http://localhost:8889/lab?token=dd69151c26a3b91fabda4b2b7e9724d13b49561f2c00908d
        http://127.0.0.1:8889/lab?token=dd69151c26a3b91fabda4b2b7e9724d13b49561f2c00908d
...
```
  + Open Jupyter in a web browser. For instance, on MacOS:
```bash
$ open ~/Library/Jupyter/runtime/jpserver-*-open.html
```

* Open a notebook, for instance
  [`ipython-notebooks/strava-fetch-and-display-activities.ipynb`](http://localhost:8889/lab/tree/ipython-notebooks/strava-fetch-and-display-activities.ipynb)
  ([source code on GitHub](https://github.com/data-engineering-helpers/strava-data/blob/main/ipython-notebooks/strava-fetch-and-display-activities.ipynb))
  + Run the cells. The last cell should display a Leaflet map with
    the activities/trips retrieved from Strava

# Use cases

## Use Jupyter Lab to retrieve trips and display them
* Open the
  [`strava-fetch-and-display-activities.ipynb` notebook](http://localhost:8889/lab/tree/ipython-notebooks/strava-fetch-and-display-activities.ipynb)
  ([`strava-fetch-and-display-activities.ipynb` source code on GitHub](https://github.com/data-engineering-helpers/strava-data/blob/main/ipython-notebooks/strava-fetch-and-display-activities.ipynb))
  + Run the cells. The last cell should display a Leaflet map with
    the activities/trips retrieved from Strava

## Use Python scripts to retrieve trips and display them
* Authenticate with the Strava API as explained in the
  [Generate an access token section](#generate-an-access-token)
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
  [`python/strava-leaflet-app/templates/leaflet.html` HTML template file](python/strava-leaflet-app/templates/leaflet.html#L19)
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

* Authenticate with the Strava API as explained in the
  [Generate an access token section](#generate-an-access-token)
  + Store the access tokem as an environment variable:
```bash
$ export STRAVA_ACCESS_TOKEN="<strava-api-access-token>"
```

### Retrieve a few details from the Strava profile
* Retrieve a few details from the Strava profile:
```bash
$ curl -s -X GET https://www.strava.com/api/v3/athlete -H "Authorization: Bearer $STRAVA_ACCESS_TOKEN" | jq
```
```javascript
{
  "id": 123456789,
  "username": null,
  "resource_state": 2,
  "firstname": "John",
  "lastname": "Doe",
  "bio": null,
  "city": "Lille",
  "state": "Nord",
  "country": "France",
  "sex": "M",
  "premium": false,
  "summit": false,
  "created_at": "2023-07-02T15:32:42Z",
  "updated_at": "2023-07-03T10:03:39Z",
  "badge_type_id": 0,
  "weight": 80,
  "profile_medium": "https://graph.facebook.com/1234567890123456/picture?height=256&width=256",
  "profile": "https://graph.facebook.com/1234567890123456/picture?height=256&width=256",
  "friend": null,
  "follower": null
}
```

### Retrieve the list of activities/trips
* Reference:
  https://developers.strava.com/docs/reference/#api-Activities-getLoggedInAthleteActivities
```bash
curl -s -X GET https://www.strava.com/api/v3/athlete/activities -H 'Authorization: Bearer 82305f579f99247b6652e41b9e42b11c4b5e1185' | jq 2>&1 | tee data.private/strava-activities.json
cat data.private/strava-activities.json | jq
```
```javascript
[
  {
    "resource_state": 2,
    "athlete": {
      "id": 123456789,
      "resource_state": 1
    },
    "name": "Evening Ride",
    "distance": 1471.8,
    "moving_time": 279,
    "elapsed_time": 279,
    "total_elevation_gain": 0,
    "type": "Ride",
    "sport_type": "Ride",
    "workout_type": 12,
    "id": 9376697877,
    "start_date": "2023-07-02T18:31:09Z",
    "start_date_local": "2023-07-02T20:31:09Z",
    "timezone": "(GMT+01:00) Europe/Paris",
    "utc_offset": 7200,
    "location_city": null,
    "location_state": null,
    "location_country": "France",
    "achievement_count": 0,
    "kudos_count": 6,
    "comment_count": 0,
    "athlete_count": 1,
    "photo_count": 0,
    "map": {
      "id": "a123456789",
      "summary_polyline": "}adtHo`yQ_@{@kA{AcEqGiNgUqEsHyBeDgDeGeDeFoK{P_@q@JUNQHCLHDC",
      "resource_state": 2
    },
    "trainer": false,
    "commute": true,
    "manual": false,
    "private": false,
    "visibility": "followers_only",
    "flagged": false,
    "gear_id": "b12769770",
    "start_latlng": [
      50.65,
      3.08
    ],
    "end_latlng": [
      50.66,
      3.09
    ],
    "average_speed": 5.275,
    "max_speed": 7.2,
	...
    "has_kudoed": false
  },
  …
]
```

* Extract a few details from the JSON file as a CSV file:
```bash
$ cat data.private/strava-activities.json | jq -r '.[]|[.id,.start_date,.name,.type,.sport_type,.distance,.elev_high,.elev_low,.moving_time,.elapsed_time,.average_speed,.max_speed,.average_watts,.kilojoules,.average_heartrate,.location_country,.timezone,.utc_offset,.start_latlng[],.end_latlng[],.private,.gear_id]|@csv'  | sed -e 's/"//g' 
123456789,2023-07-02T18:31:09Z,Evening Ride,Ride,Ride,1471.8,39.4,25.6,279,279,5.275,7.2,57.8,16.1,140.1,France,(GMT+01:00) Europe/Paris,7200,50.65,3.08,50.66,3.09,false,123456789
…
```

### Retrieve the details for a specific activity
* Reference:
  https://developers.strava.com/docs/reference/#api-Activities-getActivityById
  
* Launch cURL:
```bash
$ curl -s -X GET "https://www.strava.com/api/v3/activities/123456789" -H 'Authorization: Bearer 82305f579f99247b6652e41b9e42b11c4b5e1185' | jq 2>&1 | tee strava-activity-detail.json
```
```javascript
{
  "resource_state": 3,
  "athlete": {
    "id": 123456789,
    "resource_state": 1
  },
  "name": "Lunch Gravel Ride",
  "distance": 55984.1,
  ...
  "map": {
    "id": "a9374290388",
    "polyline": "oyfXxxxE@@@",
    "resource_state": 3,
    "summary_polyline": "_tftXxxxiDpE"
  },
  "trainer": false,
  ...
  "start_latlng": [
    50.66,
    3.10
  ],
  "end_latlng": [
    50.66,
    3.10
  ],
  "average_speed": 5.111,
  ...
  "segment_efforts": [
    {
      "id": 123456789,
      "resource_state": 2,
      "name": "Avenue de la République - Croisé-Laroche - Clémenceau (vers l'ouest)",
      "activity": {
        "id": 123456789,
        "resource_state": 1
      },
	  ...
      "segment": {
        "id": 20239919,
        "resource_state": 2,
        "name": "Avenue de la République - Croisé-Laroche - Clémenceau (vers l'ouest)",
        "activity_type": "Ride",
		...
      },
      "pr_rank": 3,
      "achievements": [
        {
          "type_id": 3,
          "type": "pr",
          "rank": 3
        }
      ],
      "hidden": false
    },
  …
  ],
  "splits_metric": [
    {
      "distance": 1000.9,
      "elapsed_time": 218,
	  ...
      "pace_zone": 0
    },
    …
  ],
  "splits_standard": [
    {
      "distance": 1610.3,
      "elapsed_time": 334,
	  ...
      "pace_zone": 0
    },
    …
  ],
  "laps": [
    {
      "id": 31984370773,
      "resource_state": 2,
      "name": "Lap 1",
	  ...
      "split": 1
    }
  ],
  "gear": {
    "id": "123456789",
    "primary": false,
    "name": "RockRider ST540 S",
	...
    "converted_distance": 1100.9
  },
  "photos": {
    ...
  },
  "stats_visibility": [
    {
      "type": "heart_rate",
      "visibility": "everyone"
    },
	...
  ],
  "hide_from_home": false,
  "device_name": "Apple Watch SE",
  ...
}
```

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
* If PySpark is to be used with Spark Connect, which makes the whole process
  more repeatable/industrial, there are some subtleties in the setup process.
  Follow the instructions on
  [GitHub - DataBricks example peoject](https://github.com/data-engineering-helpers/databricks-examples#pyspark-and-jupyter)
  for more details.

## Python environment
* It is recommended to use PyEnv and to install a fairly recent stable Python
  environment (for instance, at the time of writing, Python 3.10.17 or 3.11.4)

* Update the Pip utility, if needed:
```bash
$ python -mpip install -U pip
```

* Install a few Python libraries:
```bash
$ python -mpip install -U plotly pyvis folium
```

* Install PySpark:
```bash
$ python -mpip install -U pyspark[connect,sql,pandas_on_spark] pytest-spark
```

* Install JupterLab:
```bash
$ python -mpip install -U jupyterlab
```

* Install a few JupyterLab extensions (_e.g._, Leaflet):
```bash
$ jupyter labextension install @jupyter-widgets/jupyterlab-manager jupyter-leaflet
```

## Create an application for Strava API
To start developing with the Strava API, you will need to make an application
* If you have not already, go to https://www.strava.com/register and sign up
  for a Strava account.
* After you are logged in, go to https://www.strava.com/settings/api
  and create an app.
* You should see the “My API Application” page now. Here is what everything
  means:
  + Category: The category you chose for your application
  + Club: Will show if you have a club associated with your application
  + Client ID: Your application ID
  + Client Secret: Your client secret (please keep this confidential)
  + Authorization token: Your authorization token which will change
    every six hours (please keep this confidential)
  + Your Refresh token: The token you will use to get a new authorization
    token (please keep this confidential)
  + Rate limits: Your current rate limit
  + Authorization Callback Domain: When building your app, change
    “Authorization Callback Domain” to localhost or any domain.
	When taking your app live, change “Authorization Callback Domain”
	to a real domain.

## Authorize the application to use Strava API
* The authorization process has to be done just once every so often
* The user (you, me) has to authorize the application (this application
  we are building here) to use the Strava API. The application is known
  to Strava API and appears on https://www.strava.com/settings/apps .
  If this is not the case yet, one can easily register a new application
  to use the Strava API (on https://www.strava.com/settings/api)
* Be sure to have the following Strava API details at hand,
  from https://www.strava.com/settings/api:
  + Client ID
  + Client secret
* Save those details as environment variables (_e.g._, in the
  `~/.bashrc`/`~/.zshrc` file):
```bash
export STRAVA_CLIENT_ID="<the-strava-client-id>"
export STRAVA_CLIENT_SECRET="<the-strava-client-secret>"
export STRAVA_ACCESS_TOKEN="" # empty for now
export STRAVA_REFRESH_TOKEN="" # empty for now
```

### Generate an authorization code with the internet browser
* Get a Strava API authorization code by opening the following link
  (be careful to replace `strava-api-client-id` with your own Strava API
  client ID, which should read something like 1234567):
  + Open
    http://www.strava.com/oauth/authorize?client_id=strava-api-client-id&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=read_all,activity:read_all
  + Click on the Authorize button
  + In the URL of the just opened page (displaying an error), copy the `code`
    value, it corresponds to the Strava API authorization code
* The Strava API authorization code remains valid for a long time
  (several days). You can save it along with other passwords (_e.g._,
  in a password manager) or in a private MS Word/Google Doc/text document.
* The authorization code is then used to generate both:
  + A refresh token, which has roughly the same validity
    as the authorization code
  + An access token, which itself is valid only for a limited period
    of time (typically, a few hours).
	That access token may be re-generated as many times as needed thanks
	to the refresh token.
    The access token is what the Strava API needs to answer to API requests

## Generate an access token
Perform either of the following two tasks

### Generate the access and refresh tokens with the CLI
* To be performed when the refresh token is deprecated or when there is no refresh token yet
* Use cURL on the command-line to create the access code (and the refresh code):
```bash
curl -s -X POST https://www.strava.com/oauth/token -F client_id=$STRAVA_CLIENT_ID -F client_secret=$STRAVA_CLIENT_SECRET -F code=<strava-api-authorization-code> -F grant_type=authorization_code | jq
```
```javascript
{
  "token_type": "Bearer",
  "expires_at": 1688424735,
  "expires_in": 19659,
  "refresh_token": "1a5b02some-tokena42a15",
  "access_token": "7f988some-token950db8",
  "athlete": {
    "id": 123456789,
    "username": null,
    "resource_state": 2,
    "firstname": "John",
    "lastname": "Doe",
    "bio": null,
    "city": "Lille",
    "state": "Nord",
    "country": "France",
    "sex": "M",
    "premium": false,
    "summit": false,
    "created_at": "2023-07-02T15:32:42Z",
    "updated_at": "2023-07-03T10:03:39Z",
    "badge_type_id": 0,
    "weight": 80,
    "profile_medium": "https://graph.facebook.com/1234567890123456/picture?height=256&width=256",
    "profile": "https://graph.facebook.com/1234567890123456/picture?height=256&width=256",
    "friend": null,
    "follower": null
  }
}
```

#### Store the access and refresh tokens as environment variables
* Store the access and refresh tokens as environment variables:
```bash
export STRAVA_ACCESS_TOKEN="<strava-api-access-token>"
export STRAVA_REFRESH_TOKEN="<strava-api-refresh-token>"
```

### Refresh the access and refresh tokens with the CLI
* Use cURL on the command-line to create the access code (and the refresh code):
```bash
curl -s -X POST https://www.strava.com/oauth/token -F client_id=$STRAVA_CLIENT_ID -F client_secret=$STRAVA_CLIENT_SECRET -F refresh_token=<strava-api-refresh-token> -F grant_type=refresh_token | jq
```

#### Store the access token as environment variable
* Store the access token as an environment variable:
```bash
export STRAVA_ACCESS_TOKEN="<strava-api-access-token>"
```

