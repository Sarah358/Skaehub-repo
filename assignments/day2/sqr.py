# import math
import math
# take user input
num = int(input('Enter a number: '))
# compute sqr root
root = math.sqrt(num)

if int(root + 0.5) ** 2 == num:
    print(num, "is a perfect square")
else:
    print(num, "is not a perfect square")

