# function to determine whether a year is a leap year or not
def leap_year(y):
    # if no remainder after dividing then the year is leap so return true
    # applies to century years(those divisible by 100)
    if y % 400 == 0:
        return True
        # if the year has no remainder after dividing by 100 the its not a leap year
    if y % 100 == 0:
        return False
        # if the year is divisible by 4 then it is a leap year hence return true
    if y % 4 == 0:
        return True
    else:
        return False
# allow input
x = int(input('Enter a year ' ))
print(leap_year (x))


