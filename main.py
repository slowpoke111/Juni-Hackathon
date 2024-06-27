from getData import fetchAmenitiesOfType

#Philadelphia 
latitude = 39.9526 
longitude = -75.1652  

amenities = fetchAmenitiesOfType(latitude,longitude,"restaurant",1000)

for i in amenities:
    print(i)
