# import modules
from math import radians, cos, sin, asin, sqrt
from geopy.geocoders import Nominatim
from geopy.units import kilometers

# Radius of earth in kilometers. Use 3956 for miles
r = 6371

# get geolocator from nominatim
geolocator = Nominatim(user_agent="Get zipcode details")
# get location of nairobi
location1 = geolocator.geocode('Nairobi')
# get location of cairo
location2 = geolocator.geocode('Cairo')

# get latitudes and longitudes
lon1 =  location1.longitude
lon2 = location2.longitude
lat1 = location1.latitude
lat2 = location2.latitude

 # Haversine formula to get distance
dlon = lon2 - lon1
dlat = lat2 - lat1
a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
 
c = 2 * asin(sqrt(a))
 # calculate the result
result = (c * r)

print('The distance between Nairobi and Cairo is:')
print(int(result))


