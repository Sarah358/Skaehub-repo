# import requests module
import requests
# execute the request
response = requests.get('http://example.com/') 
# print response of google
print('The response')
print(response.text)
print("\n .....................................................")  #seperate the outputs 
# print content of url
print('\n content of url')
print(response.content)
print('\n..................................')
# raw 
print('\n Raw data of url')
r = requests.get('https://medium.com/new-story', stream = True)
# print raw data of url
print(r.raw)
print(r.raw.read(15))










# url
# url = 'https://jsonplaceholder.typicode.com/todos/1' 
# execute get request
# response = requests.get(url)
# print response
# print(response.status_code) 
# printed formated json file
# print(response.text)   