from getData import *
import utils

#latitude = 40.1546
#longitude = -75.2216

latitude, longitude = utils.zipToLatLong(19002)
amenities = fetchAmenitiesOfType(latitude,longitude,"restaurant",5000)

for i in amenities:
    print(i)

print(getRainChance(latitude,longitude))