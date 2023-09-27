# Raise our own expectons
def colorize(text,color):
    colors = ('cyan','yellow','blue','green','magenta')
    if type(color) is not str:
        raise TypeError("color must be an instance of str")
    if type(text) is not str:
        raise TypeError("text must be an instance of str")
    if color not in colors:
        raise ValueError("Invalid color")
    print(f"Printed {text} in {color}")

colorize([],"cyan") 
# colorize(34,'red')