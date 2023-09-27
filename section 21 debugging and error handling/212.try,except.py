# MORE SYNTAX 
# try:
# except:
# else: runs when except does not.
# finally: runs no matter what

while True:
    try:
        num = int(input("please enter a number: "))
    except ValueError:
        print("That's not a number!")
    else: #runs when except does not.
        print("Good job!,you entered a number") 
        break
    finally:
        print("runs no matter what!")
print("REST OF THE GAME LOGIC RUNS!")

# try:
#     num = int(input("please enter a number: "))
# except:
#     print("That's not a number!")
# else: #runs when except does not.
#     print("Im in the else!") 
# finally:
#     print("runs no matter what!")