# import requests
import requests
# show the timeout message
print("\n timeout = 1.0")    
try:
    # get response of url page
    res = requests.get('https://medium.com/', timeout = 1.0)
    # print response in text format
    print(res.text )
    
except requests.exceptions.RequestException as e:
    # print error message
    print('timeout',e)