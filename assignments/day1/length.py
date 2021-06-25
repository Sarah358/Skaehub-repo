def len_last_word(a):
    # split the words and give a seperator which is space
    arr = a.split(' ')
    # check size of the word
    size = len(arr)
    # if the size is 1 return the length of that word
    # 
    if size==0:
        return 0
    return len(arr[-1])

    # allow input from user
print('Write a statement')    
a = input()
# call the function
len_last_word(a)
print(len_last_word(a))
