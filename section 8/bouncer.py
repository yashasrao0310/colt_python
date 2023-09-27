age = input("How old are you? ")

if age:
    age =int(age)
    if age >= 21:
        print("You can anter and drink")
    elif age >= 18:
        print("You can enter but need a wristband!")
    else:
        print("Sorry little one, you casnnot enter")
else:
    print("Invalid input, please enter an age")