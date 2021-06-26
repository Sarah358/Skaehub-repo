# getting city,state and country of specified lat and long
# import modules
from geopy.geocoders import Nominatim
# initializing nominatim
geolocator = Nominatim(user_agent="Get data from lat and long")
# reverse the location and get the lat and long
location = geolocator.reverse("52.509669, 13.376294")
# print address
print(location.address) 