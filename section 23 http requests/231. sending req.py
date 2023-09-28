# query string - a way to apss data tothe server as part of a GET req
# https://www.example.com/?key1=value1&key2=value2
import requests
url = "https://icanhazdadjoke.com/search" 

response = requests.get(url ,
                        headers={'Accept':'application/json'},
                        params = {'term':'cat','limit':1})

data = response.json()
print(data['results'])

# print(data['joke']) 
# print(f"status:{data['status']}")