names = ["Jane", "Doe", "John", "Stan"]
# function to iterate through the list
def display_data():
    for name in names:
        print("My name is", name)
    display_data()
    # call the function
display_data()
