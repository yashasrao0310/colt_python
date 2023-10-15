# 2 differernt ways to write:
    # 1.using lists
    # 2.using dicts
    
# writer - creates writer object for writing into csv 
# writerow - method on a writer to write a row on the csv

# ex1
from csv import writer
with open("cats.csv",'w') as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Name", "Age"])
    csv_writer.writerow(["Blue", 3])
    csv_writer.writerow(["Kitty", 1])
    
# with open("fighters.csv") as file:
#     csv_writer = reader(file)
#     for row in csv_writer:
#         print(row)