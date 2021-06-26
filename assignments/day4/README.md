# Question one

```Write a Python program to find the details of a givenzip code using theNominatim API and GeoPy package```

- Import the necessary modules ie geopy.geocoders from nominatim.
- Next get zipcode details using nominatim module.
- Allow user to input zipcode
-Geolocator then gets the location of the zipcode input and prints adress, latitide and longitude. As illustrated below

![2021-06-26 11-45-47](https://user-images.githubusercontent.com/60597568/123507829-5a08ab00-d674-11eb-8528-bd50dbcda0fe.gif)

# Question two

```Write a Python program to calculate the distance betweenCairo and Nairobi City ```

## import modules
 - Math module to do computation
 - NOminatim module to getlocation
 - Geounits module to get the units of distance
 
 define a variable with the radius of the earth in kilometres
 ### Get distance
 
 1. Get the location of nairobi and cairo using geolocator.
 2. Get the latitudes and longitudes af the locations
 3. use the haversine formula to calculate distance
     ```
     Haversine formula
     
     dlon = lon2 - lon1
      dlat = lat2 - lat1
      a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
      c = 2 * asin(sqrt(a))
      ```
 4. Calculate result using formula
     ```result = (c * r) ```
  5. Print result as illustrated below.    
 


