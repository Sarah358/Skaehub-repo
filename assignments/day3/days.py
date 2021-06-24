# get yesterday,today and tomorrow
import numpy as np

# for today
today = np.datetime64('today', 'D')
print("Today is: ", today)

# for yesterday subtract a day from today
yesterday = np.datetime64('today', 'D')- np.timedelta64(1, 'D')
- np.timedelta64(1, 'D')

print("Yesterday was: ", yesterday)

# for tomorrow add a day to today
# add t
tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
+ np.timedelta64(1, 'D')

print("Tomorrow is: ", tomorrow)

