import requests

url = 'http://127.0.0.1:8000/car/list'

getresponse = requests.get(url)
print(getresponse.json())
print(getresponse.status_code)