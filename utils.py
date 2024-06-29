import pandas as pd
import requests
from requests.exceptions import HTTPError

zipcodes = pd.read_csv("zip_lat_long.csv")  # https://www.kaggle.com/datasets/joeleichter/us-zip-codes-with-lat-and-long


def zipToLatLong(zip_code: int):
    matching_row = zipcodes.loc[zipcodes["ZIP"] == zip_code]

    if not matching_row.empty:
        lat = matching_row.iloc[0]["LAT"]
        lng = matching_row.iloc[0]["LNG"]
        return lat, lng
    else:
        raise Exception("No lat/long found for input")  # change to none later
        # return None, None


def miToMeters(miles: float) -> float:
    return miles * 1609.344

#https://nominatim.org/release-docs/latest/api/Reverse/
def latLongtoAddress(lat:float,long:float,params=""):
    url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={long}&params={params}&format=json"
    try:
        response = requests.get(url,headers={'User-Agent': 'YourAppName/1.0 (slow111poke@gmail.com)'}) # create actual header later
        response.raise_for_status()  # Handle status codes between 400-600

    except HTTPError as http_err:
        raise HTTPError(f"{http_err} in url")
    except Exception as e:
        raise Exception(f"Error: {e} in url")
    else:
        text = response.json()
        return {"displayName":text["display_name"],"address":text["address"]}
