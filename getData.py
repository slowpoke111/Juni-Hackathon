import overpy
import requests
from requests.exceptions import HTTPError
import json

def _fetchAmenitiesOfType(latitude:float, longitude:float, amenity_type:str, radius:int):
    api = overpy.Overpass()
    
    
    query = f"""
        [out:json];
        node(around:{radius},{latitude},{longitude})["amenity"="{amenity_type}"];
        out;
    """
    
    result = api.query(query)
    return result

def fetchAmenitiesOfType(latitude:float, longitude:float, amenity_type:str, radius:int) -> list[dict]:
    amenities = _fetchAmenitiesOfType(latitude, longitude, amenity_type, radius)
    amenitiesList = []
    for node in amenities.nodes:
        name = node.tags.get('name', 'Unnamed')  # Defualt to unnamed
        amenitiesList.append({"amenityType":amenity_type, "name": name, "lat":float(node.lat), "lon":float(node.lon)})
    
    return amenitiesList

#https://api.weather.gov/gridpoints/PHI/46,85/forecast
def _getRainChance(url,period=0):
    try:
        response = requests.get(url)
        response.raise_for_status() 

    except HTTPError as http_err:
        raise HTTPError(f"{http_err} in forecast url")
    except Exception as e:
        raise Exception(f"Error: {e} in forecast url")
    else:
        x = response.json()["properties"]["periods"][period]["probabilityOfPrecipitation"]["value"]
        return 0 if x==None else int(x)
#https://api.weather.gov/gridpoints/PHI/46,85/forecast

def getRainChance(lat:float,long:float,period:int=0):
    baseURL = f"https://api.weather.gov/points/{lat},{long}"

    try:
        response = requests.get(baseURL)
        response.raise_for_status() #Handle status codes between 400-600 

    except HTTPError as http_err:
        raise HTTPError(f"{http_err} in base url")
    except Exception as e:
        raise Exception(f"Error: {e} in base url")
    else:
        return _getRainChance(response.json()["properties"]["forecast"], period)


"""
latitude = 39.9526 
longitude = -75.1652  
amenity_type = "restaurant"  # https://wiki.openstreetmap.org/wiki/Key:amenity
radius = 1000  # Radius in meters

if __name__ == "__main__":
    amenities = _fetchAmenitiesOfType(latitude, longitude, amenity_type, radius)

    for node in amenities.nodes:
        name = node.tags.get('name', 'Unnamed')  # Defualt to unnamed
        print(f"{amenity_type}: {name} ({node.lat}, {node.lon})")
"""