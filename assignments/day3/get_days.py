import numpy as np
print('Enter From Day YYYY-MM e.g 2021-07')
# allow user to input the start date 
start_count = input()
print('Enter To Day YYYY-MM e.g 2021-07')
# allow user to input stop day
stop_count = input()
# count number of weekdays from startcount to stopcount
s= np.busday_count(start_count, stop_count)
# print number of weekdays 
print('Number of weekdays : ')
print(s)

