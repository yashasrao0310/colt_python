# beautiful soup lets us navigate through html with python
# beautiful soup does NOT download html - for this we need request module

# note: html comes back as a giant string from the request module 
# beautiful soup also supports parsing XML

# parsing and navigating html 
# BeautifulSoup(html_string , "html.parser") - parse html
# Once parsed, there are several ways to navigate:
# by TagName
# Using find - returns one matching tag 
# using find_all - returns list of matching tags 

from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>First HTML Page</title>
</head>
<body>
< div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
</>
<ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
</ol>
<div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser") #parsed data(html) into string
# print(soup.body.div)
# d = soup.find("li")
# d = soup.find_all(class_="special")
# d = soup.find_all(attrs={"data-example":"yes"})
# # print(type(d))
# print(d)

# print(type(soup)) #return onstance of class BeautifulSoup on which methods can be used - <class 'bs4.BeautifulSoup'>

# select - returns a list of elements matching a CSS selector
# Selector cheatsheet
# #id and .class
# select children: div > p
# select descendents: div p

b = soup.select("#first") #select alwsys gives a list back
print(b)