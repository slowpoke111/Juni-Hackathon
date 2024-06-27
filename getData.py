import overpy

def fetchAmenitiesOfType(latitude, longitude, amenity_type, radius):
    api = overpy.Overpass()
    
    
    query = f"""
        [out:json];
        node(around:{radius},{latitude},{longitude})["amenity"="{amenity_type}"];
        out;
    """
    
    result = api.query(query)
    return result

latitude = 40.1546 
longitude = -75.2216  
amenity_type = "restaurant"  
radius = 1000  # Radius in meters

if __name__ == "__main__":
    amenities = fetchAmenitiesOfType(latitude, longitude, amenity_type, radius)

    for node in amenities.nodes:
        name = node.tags.get('name', 'Unnamed')  # Defualt to unnamed
        print(f"{amenity_type}: {name} ({node.lat}, {node.lon})")
