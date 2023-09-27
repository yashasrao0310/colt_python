import requests

# itr1
# url = "https://www.google.com/adas/asd"
# response = requests.get(url)  #404

url = "https://www.google.com"
response = requests.get(url) #200

# url = "www.google.com"  #if no https we can't req that website
# response = requests.get(url) #Invalid URL 'www.google.com': No scheme supplied. 
# #Perhaps you meant https://www.google.co

print(f'your request to {url} came back w/ status code {response.status_code}')

print(response.text) #for human - html and js