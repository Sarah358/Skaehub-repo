# import the modules
import random
import string

# define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

# combine data
all = lower + upper + num + symbols

while 1:
    password_len = int(input('What length would you like your password to be?  '))
    # ask how many times the user wants the password to be generated
    password_count = int(input('How many passwords do you want? '))
    # loop through until password_count
    for x in range(0,password_count) :
        password = ''
        for x in range(0,password_len):
            temp = random.choice(all)
            # append the password characters
            password = password + temp
            print(password)
