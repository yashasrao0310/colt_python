# Dictwriter - createes a new object for writing using dictionaries
# fieldname - kwarg for the DictWriter specifying headers
# writeheader - method on a writer to write header row
# writerow - method on a writer to write a row based on a dictionary

# ex1
# from csv import DictWriter

# with open("example.csv","w",newline='') as file:
#     headers = ["Character","Move"]
#     csv_writer = DictWriter(file, fieldnames=headers)
#     csv_writer.writeheader()
#     csv_writer.writerow({
#         "Character":"Ryu",
#         "Move":"Hakouden"
#     })

# ex2
from csv import DictWriter

with open("cats.csv","w",newline='') as file:
    headers = ["Name","Age","Breed"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    # values don't need to be in order
    csv_writer.writerow({
        "Name":"Garfield",
        "Breed":"Persian",
        "Age":10
    })
    