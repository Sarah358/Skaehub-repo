# Question one

```Write a Python program to find the details of a givenzip code using theNominatim API and GeoPy package```

- Import the necessary modules ie geopy.geocoders from nominatim.
- Next get zipcode details using nominatim module.
- Allow user to input zipcode
-Geolocator then gets the location of the zipcode input and prints adress, latitide and longitude. As illustrated below

get full code from get_details.py file

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
  
  get full code from get_distance.py file
  
  ![2021-06-26 12-09-39 (1)](https://user-images.githubusercontent.com/60597568/123508425-0b5d1000-d678-11eb-845a-5828109d0df0.gif)
  
  # Question three
  
  ```Write a Python function to get the city, state andcountry name of a specifiedlatitude and longitude using Nominatim API and Geopypackage. ```
  
  1. import niminatim
  2. Use the reverse method in geolocator to input the latitude and longitude:
     ```location = geolocator.reverse("52.509669, 13.376294") ```
  3.Print the location address of the latitude and longitude.As illustrated below.
  
  get full code from get_data.py file
  
  ![question_3](https://user-images.githubusercontent.com/60597568/123509692-a3122c80-d67f-11eb-8b9f-72f1581c7b13.gif)




  
  # Question 4
  
  ```Write a Python program to search the country namefrom a given state nameusing the  Nominatim API and GeoPy package```
  
  1. import niminatim module
  2. Prompt user to input a state name
  3. split the address location and print the last index of the address which is the country as illustrated below.
 
get full code from get_country.py file

![country](https://user-images.githubusercontent.com/60597568/123509701-ab6a6780-d67f-11eb-814e-3f4762bdf5c1.gif)

# Question five

```Write a Python program to generate an infinite cycleof elements from an iterable.

PS:The iterable data type should be a list or a stringor a dictionary, etc

```
1. Create a list and assign it to a variable.
2. Define a function and loop through the items recursively. Read obout recursion on the python documentation.
3. call the function and print the list as illustrated below.
Get full code on recursion.py file.

![question_5](https://user-images.githubusercontent.com/60597568/123509710-b1f8df00-d67f-11eb-951f-a4acd7e4b0b9.gif)

# Question six.

```Write a Python program to sort a list of dictionariesusing Lambda ```

1. Create a list of dictionaries and assign it to a variable.
2. print the list to preview it.
3. Sort the list and use lambda funtion to sort by using a specific key in the dictionary
4. print the sorted list as illustrated below.


![question_6](https://user-images.githubusercontent.com/60597568/123509714-bae9b080-d67f-11eb-8784-ef887dc6a5d6.gif)

# Question seven

```Write a Python program to find the maximum and minimumvalues in a given listof tuples using a lambda function ```

1. Define a function to get min and max values
2. Use lambda function to get the max and min and return the values.
3. ASign a list of tuples to a variable .
4. call the function and parse the list as an argument.
5. This prints the max and minimum values as illustrated below.

get full code at get_min_max.py file in my repo


![question_7](https://user-images.githubusercontent.com/60597568/123509718-c0df9180-d67f-11eb-8f75-4e70435325ae.gif)

  
 


