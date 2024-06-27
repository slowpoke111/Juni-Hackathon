import overpy

def _fetchAmenitiesOfType(latitude, longitude, amenity_type, radius):
    api = overpy.Overpass()
    
    
    query = f"""
        [out:json];
        node(around:{radius},{latitude},{longitude})["amenity"="{amenity_type}"];
        out;
    """
    
    result = api.query(query)
    return result

def fetchAmenitiesOfType(latitude, longitude, amenity_type, radius):
    amenities = fetchAmenitiesOfType(latitude, longitude, amenity_type, radius)

    for node in amenities.nodes:
        name = node.tags.get('name', 'Unnamed')  # Defualt to unnamed
        return {"amenity":amenity_type, "name": name, "lat":node.lat, "lon":node.lon}

latitude = 39.9526 
longitude = -75.1652  
amenity_type = "restaurant"  # https://wiki.openstreetmap.org/wiki/Key:amenity
radius = 1000  # Radius in meters

if __name__ == "__main__":
    amenities = fetchAmenitiesOfType(latitude, longitude, amenity_type, radius)

    for node in amenities.nodes:
        name = node.tags.get('name', 'Unnamed')  # Defualt to unnamed
        print(f"{amenity_type}: {name} ({node.lat}, {node.lon})")
