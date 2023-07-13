#
# File: https://github.com/data-engineering-helpers/strava-data/blob/main/python/strava-leaflet-app/strava-authenticate.py
#
# Inspired from https://developer-old.byu.edu/docs/consume-api/use-api/oauth-20/oauth-20-python-sample-code
#
__author__ = 'Denis Arnaud'

import requests, json
import subprocess
import sys
import os

authorize_url = "http://www.strava.com/oauth/authorize"
token_url = "https://www.strava.com/oauth/token"

#callback url specified when the application was defined
callback_uri = "http://localhost/exchange_token"

# Strava API to be called once authenticated
test_api_url = "https://www.strava.com/api/v3/athlete"

# Strava client (application) credentials (https://www.strava.com/settings/api)
client_id = os.getenv("STRAVA_CLIENT_ID")
client_secret = os.getenv("STRAVA_CLIENT_SECRET")

#step A - simulate a request from a browser on the authorize_url - will return an authorization code after the user is
# prompted for credentials.

authorization_redirect_url = (
    f"{authorize_url}" +
    f"?client_id={client_id}" +
    f"&response_type=code" +
    f"&redirect_uri={callback_uri}" +
    f"&approval_prompt=force" +
    f"&scope=read_all,activity:read_all"
    )

print("go to the following url on the browser and enter the code from the returned url: ")
print("---  " + authorization_redirect_url + "  ---")
authorization_code = input('code: ')

# step I, J - turn the authorization code into a access token, etc
data = {
    "client_id": client_id,
    "client_secret": client_secret,
    'code': authorization_code,
    "grant_type": "authorization_code"
}
print("Requesting access token...")
access_token_response = requests.post(token_url,
                                      data=data,
                                      verify=False,
                                      allow_redirects=False,
                                      auth=(client_id,
                                            client_secret))

print("... Response:")
print(f"  * Header: {access_token_response.headers}")
print(f"  * Body: {access_token_response.text}")

# We can now use the access_token as much as we want to access
# protected resources.
tokens = json.loads(access_token_response.text)
access_token = tokens["access_token"]
print(f"Access token: {access_token}")

api_call_headers = {"Authorization": f"Bearer {access_token}"}
api_call_response = requests.get(test_api_url,
                                 headers=api_call_headers,
                                 verify=False)

print(api_call_response.text)

