from getData import *
import utils

# latitude = 40.1546
# longitude = -75.2216

indoorActivities = ["restaurant","arts_centre","cinema","exhibition_centre","music_venue","planetarium","theatre"]
outdoorActivities = ["ice_cream","stage"]

latitude, longitude = utils.zipToLatLong(19002)
radius = 5

#amenities = fetchAmenitiesOfType(latitude, longitude, "restaurant", utils.miToMeters(1.5))
amenities = fetchAmenitiesOfTypeMultipile(latitude, longitude, indoorActivities, utils.miToMeters(radius))

if getRainChance(latitude, longitude) < 20:
    for x in fetchAmenitiesOfTypeMultipile(latitude, longitude, outdoorActivities, utils.miToMeters(radius)):
        amenities.append(x)

for i in amenities:
    print(i)