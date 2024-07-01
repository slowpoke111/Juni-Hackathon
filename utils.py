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
def latLongtoAddress(lat: float, long: float, api_key: str, params: str = "") -> dict:
    url = f"https://api.geoapify.com/v1/geocode/reverse?lat={lat}&lon={long}&{params}&format=json&apiKey={api_key}"
    
    try:
        headers = {'User-Agent': 'YourAppName/1.0 (slow111poke@gmail.com)'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses

    except requests.HTTPError as http_err:
        raise requests.HTTPError(f"HTTP error occurred: {http_err}")

    except Exception as err:
        raise Exception(f"Other error occurred: {err}")

    else:
        data = response.json()
        print(data)
        if 'features' in data and data['features']:
            first_feature = data['features'][0]
            return {
                "displayName": first_feature['properties'].get('formatted', ''),
                "address": first_feature['properties'].get('address', {})
            }
        else:
            raise Exception("No address found in the response")