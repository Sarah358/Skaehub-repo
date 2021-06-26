from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="Get zipcode details")
print('\n\nEnter a zip code eg Nairobi 00100')
# allow user input 
zipcode = input()
# geolocator gets the location of the zipcode 
location = geolocator.geocode(zipcode)
# print the address 
print('\n\nLocation of zipcode: \n')
print(location.address)
# print latitude and longitude 
print('\n\nLatitude and Longitude:  \n')
print((location.latitude, location.longitude))
# get all raw data of the zip code and convert it into a list 
print('\n\nRaw data of the zipcode: \n ')
raw_details = (location.raw)
raw_list = list(raw_details.items())
print(raw_list)
