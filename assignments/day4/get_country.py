from re import split
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="Get country of state")
print('Enter a state name: ')
statename = input()

# geolocator gets the location of the zipcode 
location = geolocator.geocode(statename)
# get the address
details = location.address
# split details
splitted_details = details.split(',')
# print the last index of the address which is the country
print('The country name of {} is: '.format(statename))
print(splitted_details[-1])


