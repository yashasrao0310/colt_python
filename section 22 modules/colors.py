# dir(obj) and help(obj) - built in functions
from termcolor import colored

# print(dir(termcolor)) #dir() - gives list of all names associated with a package/module
# help(termcolor) 
text = colored("Hi there", color='cyan')
print(text) 

text = colored("Hi there", color='magenta')
print(text) 

text = colored("Hi there", color='yellow' ,on_color='on_cyan', attrs=["blink"])
print(text) 