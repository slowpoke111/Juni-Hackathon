import pandas as pd
zipcodes=pd.read_csv("zip_lat_long.csv") #https://www.kaggle.com/datasets/joeleichter/us-zip-codes-with-lat-and-long

def zipToLatLong(zip_code: int):
    matching_row = zipcodes.loc[zipcodes['ZIP'] == zip_code]
    
    if not matching_row.empty:
        lat = matching_row.iloc[0]['LAT']
        lng = matching_row.iloc[0]['LNG']
        return lat, lng
    else:
        raise Exception("No lat/long found")
        #return None, None 