# import random module
import random
# set range
num=random.randrange(0,100)
# guess check
guessCheck="Wrong"

while guessCheck == "Wrong":
    response = int(input('Please input a number between 0 and 100:  '))
    try:
        # allow int inputs 
        val = int(response)
    except ValueError:
        # print error if input is not an int
        print('{} is not a valid integer. Please try again'.format(val))
        continue

    val=int (response)
    if val<num:
        print("{} is lower than actual number.Please try again ".format(val))
    elif val>num:
        print("{} is higher than actual number. Please try again.".format(val))
    else:
        print('Congratulations!!! {} is the number'.format(val))
        guessCheck="correct"
        
print("Thank you for playing Number Guess. See you again")


	

