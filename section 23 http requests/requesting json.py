import requests
# headers = kwargs 
# data types of kwargs - text/plain and text/html

#only this specific website that allows API to get jokes 
# url = "https://icanhazdadjoke.com/"
# response = requests.get(url ,headers={'Accept':'text/plain'}) #gives text i.e. joke only

# print(type(response.text)) #<class 'str'>

# print(response.json()) #json to python
# JSON - data type that can be very turned n used by python
url = "https://icanhazdadjoke.com/"
response = requests.get(url ,headers={'Accept':'application/json'})

data = response.json() # '{}' to {} - gives bac a python dict - and now we can access its properties
print(type(data)) #<class 'dict'>
print(data['joke']) #joke
print(f"status:{data['status']}")