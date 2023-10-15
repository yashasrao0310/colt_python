from csv import reader, writer

# method1 - seaprate with blocks - focus on num(available not scope issue)
# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     fighters = [[s.upper() for s in row] for row in csv_reader]
#     num = 1
#     for row in fighters:
#         print(row)

# with open("screaming_fighters.csv",'w',newline='') as file: # newline='' prevents gaps between lines in writing
#     csv_writer = writer(file)
#     print(num)
#     for fighter in fighters:
#         csv_writer.writerow(fighter)

# method2 - nesting
with open("fighters.csv") as file:
    csv_reader = reader(file)
    with open("screaming_fighters.csv",'w',newline='') as file: # newline='' prevents gaps between lines in writing
        csv_writer = writer(file)
        for fighter in csv_reader:
            csv_writer.writerow([s.upper() for s in fighter])

