import googlemaps #Uses google api
import env

#import pandas as pd (For dataframe use for saving favorite spots?)

#encoding url
from urllib.parse import urlencode
from pandas.core import base
#requests to server?
import requests

#take apart link
from urllib.parse import urlparse, parse_qsl

# Save this to another file later? If uploaded on git hub
# API_KEY =  API KEY SET from google api account


#Creates client
API_KEY = env.API_KEY
map_client = googlemaps.Client(API_KEY)

data_type = "json"

startpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
endpoint = {"Address" : "1600 Amphitheatre Parkway, Mountain View, CA", "key" : API_KEY}

url_params = urlencode(endpoint)

url = f"{startpoint}?{url_params}"


# extracts the lat and long of address code
def extract_lat_long(adddress_code, data_type = "json"):
    
    startpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    endpoint = {"Address" : adddress_code, "key" : API_KEY}

    url_params = urlencode(endpoint)
    url = f"{startpoint}?{url_params}"

    req = requests.get(url)
    if req.status_code not in range(200,299):
        return {}
    lat_long = {}
    try:
        lat_long = req.json()['results'][0]['geomatry']['location']
    except:
        pass
    return lat_long.get('lat'), lat_long.get('lng')

#sample_geocoding = "https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY"

extract_lat_long("1600 Amphitheatre Parkway, Mountain View, CA")
#home_address = '8550 Braun Knoll, San Antonio, TX'
#response = map_client.geocode(home_address)


# Doing the reverse
# get starting query string from a maps html
to_parse = ""

urlparse(to_parse)

parse_url = urlparse(to_parse)
query_string = urlparse(to_parse).query
#get query from string
#query_string

query_tuple = parse_qsl(query_string)
query_dict = dict(query_tuple)

endpoint = f"{parse_url.scheme}://{parse_url.netloc}{parse_url.path}"


#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------
'''
Places Google API USAGE
'''
lat, lng = 37.42230960000001, -122.0846244
base_endpoint_places = "https://maps.googleapis.com/maps/api/place/json"
params = {"key": API_KEY,
        "input": "Mexican food",
        "inputtype": "textquery",
        "fields" : "address_component,name,geometry,permanently_closed"
        }

locationbais = f"point: {lat}, {lng}"
use_circular = False
if use_circular:
    radius = 10000
    locationbais = f"circle: {radius}@{lat},{lng}"
params_encoded = urlencode(params)

places_endpoint = f"{base_endpoint_places}?{params_encoded}"

r = requests.get(places_endpoint)
r.json()


'''
Places Nearby API USAGE
'''
# Nearby places api search
#https://maps.googleapis.com/maps/api/place/nearbysearch/output?parameters
places_endpoint2 = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
params2 = {"key": API_KEY,
        "location": f"{lat}, {lng}",
        "radius": 1500,
        "keyword" : "Mexican food"
        }
params_2_encoded = urlencode(params2)

places_url2 = f"{places_endpoint2}?{params_2_encoded}"

r2 = requests.get(places_url2)
r2.json()