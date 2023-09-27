# ex1
def fav_color(**kwargs):
    print(kwargs)
    for person, color in kwargs.items():
        print(f"{person}'s favorite color is {color}")
        print(end="\n")
    
fav_color(yashas="purple",ramesh="red",kalpesh="green")
fav_color(yashas="purple",ramesh="red",kalpesh="green",ted="blue")
fav_color(yashas="red is amazing")

# ex2
def special_greeting(**kwargs):
    if "David" in kwargs and kwargs["David"] == "special":
        return "You get a special greeting!"
    elif "David" in kwargs:
        return "Hello David"

    return "not sure who this is..."
        
print(special_greeting(David="Hello"))
print(special_greeting(BOB="Hello"))
print(special_greeting(David="special"))
print(special_greeting(Heather="hello",David="special"))