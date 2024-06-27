from getData import *

latitude = 40.1546
longitude = -75.2216

amenities = fetchAmenitiesOfType(latitude,longitude,"restaurant",1000)

for i in amenities:
    print(i)

print(getRainChance(latitude,longitude))