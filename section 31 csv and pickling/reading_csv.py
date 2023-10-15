# csv - popular data format for tabular data(most used- homogenous data thta follows a pattern) - comma separated values
# way to take tabular data and then sticking it into a file and interpret it(crime data, credit card transactions, etc)

# python has builtin csv module to read csv files 
# 2 different ways of reading csv:
    # 1.reader = lets you ierate over rows of the CSV as lists.
    # 2.DictReader - lets you iterate over rows of the CSV as OrderedDicts.

# ex1 - using reader
# from csv import reader

# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     # print(csv_reader)  #csv reader object - iterator.(as in generator where you move forward once with next() method)
#     next(csv_reader) #to avoid header
#     for fighter in csv_reader:
#         print(f"{fighter[0]} is from {fighter[1]}")
#         # each row is a list 
#         # print(row)
#     # for fighter in csv_reader:  #does nothing as iterator already moved through once
#     #     print(f"{fighter[0]} is from {fighter[1]}")
    
#     # storing data as a list to use later
# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     data = list(csv_reader)
#     print(data)  #list of lists
    
# ex2 - using DictReader
# from csv import DictReader        

# with open("fighters.csv") as file:
#     csv_reader = DictReader(file)
#     for row in csv_reader:
#         # each row is an OrderedDict - iterator - so can go through it only once.
#         # keys are automatically set up to be the headers - which can be used to access values
#         print(row['Name'])
        
# NOTE: other delimiters - Readers accept a delimiter kwarg in case your data isn't separated by commas
from csv import reader
with open("fighters2.csv") as file:
    csv_eader = reader(file, delimiter="|")
    for row in csv_eader:
        print(row)
