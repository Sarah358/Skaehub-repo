# a function to remove duplicates from a list with list as an argument

def rm_duplicate(x):
    # create a dictionary using list items as keys
    return list(dict.fromkeys(x))

# create a list and call the func
fruits = rm_duplicate(['apple','banana','mango','apple','kiwi'])

# print the unduplicated list
print(fruits)
