def test(n):
    if n<=0:
        return False
    while n%4 ==0:
        n = n/4
    if n==1:
        return True
    else:
        return False

x = int(input('Enter a number :' ))

# call the function
output = test(x)
print(output)



