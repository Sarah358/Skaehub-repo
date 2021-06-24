import numpy as np
# create an empty array
lst = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
# allow input of elements and tell the user how many elements they are inputing
    ele = int(input("Input {} elements \n".format(n)))
 
    lst.append(ele) # adding the element
     
print(lst)
# allow numpy to handle the array
x = np.array(lst)
print("Size of the memory occupied by the said array:")
# print size in bites
print("%d bytes" % (x.size * x.itemsize))

