import googlemaps #Uses google api
import env

#import pandas as pd (For dataframe use for saving favorite spots?)

#encoding url
from urllib.parse import urlencode
from pandas.core import base
#requests to server?
import requests




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



#extract_lat_long("1600 Amphitheatre Parkway, Mountain View, CA")

# Here we would want to get our home address or set it via input to get lat long of area near by you
#home_address = env.home_address
#response = map_client.geocode(home_address)


# Doing the reverse
# get starting query string from a maps html
#take apart link
from urllib.parse import urlparse, parse_qsl
to_parse = "https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY"

#urlparse(to_parse)

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
Places Google API USAGE Specific Place
'''
lat, lng = 37.42230960000001, -122.0846244
base_endpoint_places = "https://maps.googleapis.com/maps/api/place/json"
params = {"key": API_KEY,
        "input": "Mexican food",
        "inputtype": "textquery",
        "fields" : "formatted_address,name,geometry,permanently_closed"
        }

locationbais = f"point: {lat}, {lng}"
use_circular = False
if use_circular:
    radius = 10000 # Measured By meters
    locationbais = f"circle: {radius}@{lat},{lng}"
params_encoded = urlencode(params)

places_endpoint = f"{base_endpoint_places}?{params_encoded}"
#print(places_endpoint)
r = requests.get(places_endpoint)
#print(r.status_code)
# Returns Dictionary
#r.json() 


'''
Places Nearby API USAGE Give all loctions in a dictonary
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
#Returns Dictionary
#r2.json()

# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------

'''
Creating Google map Client APi
'''

class GoogleMapsClient(object):
    lat = None,
    lng = None

    data_type = "json"
    location_query = None
    api_key = None 

    def __init__(self , api_key = None, address_or_postal_code = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if api_key == None:
            raise Exception("API KEY IS REQUIRED!")
        self.api_key = api_key
        self.location_query = address_or_postal_code
        if self.location_query != None:
            self.extract_lat_long()



    # Gets Lat and long
    def extract_lat_long(self, location = None):
        location_query = self.location_query
        if location != None:
            location_query = location

        endpoint = f"https://maps.googleapis.com/maps/api/geocode/{self.data_type}"
        params = {"Address" : location_query, "key" : self.api_key}

        url_params = urlencode(params)
        url = f"{endpoint}?{url_params}"

        req = requests.get(url)
        if req.status_code not in range(200,299):
            return {}
        lat_long = {}
        try:
            lat_long = req.json()['results'][0]['geomatry']['location']
        except:
            pass
        lat, lng = lat_long.get('lat'), lat_long.get('lng')
        self.lat = lat
        self.lng = lng
        return lat, lng

    # Gets list of locations nearby
    def search(self, keyword= "Mexican food", location = None, radius = 1000):
        lat, lng = self.lat, self.lng
        if location != None:
            lat, lng = self.extract_lat_long(location = location)
        endpoint = f"https://maps.googleapis.com/maps/api/place/nearbysearch/{self.data_type}"
        params = {"key": self.api_key,
            "location": f"{lat}, {lng}",
            "radius": radius,
            "keyword" : keyword
        }
        params_encoded = urlencode(params)

        places_url = f"{endpoint}?{params_encoded}"

        r = requests.get(places_url)
        if r.status_code not in range(200,299):
            return {}
        return r.json()

    # Gets detail locations from place (name, rating, phone number, and address)
    # need a location Id
    def deatil(self, place_id = "", fields = ["name", "rating", "formatted_phone", "formatted_address"]):
        detail_base_endPoint = "https://maps.googleapis.com/maps/api/place/details/{self.data_type}"
        detail_params = {
            "place_id" : f"{place_id}",
            "fields" : ",".join(fields),
            "key" : self.api_key
        }
        detail_params_encoded = urlencode(detail_params)
        detail_url = f"{detail_base_endPoint}?{detail_params_encoded}"
        r = requests.get(detail_url)
        if r.status_code not in range(200,299):
            return {}
        return r.json()


# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------

# client = GoogleMapsClient(api_key = Google_API_KEY, address_or_postal_code = 'city, state')
# print(client.lat, client.lng)

#client = GoogleMapsClient(API_KEY = API_KEY, address_or_postal_code= '')
#print(client.lat, client.lng)

#client.search("Tacos", "San Antonio")