# Parameter ordering is the order in which paarameters are passed into
# a function while declaring it so the code doesn't break 
def display_info(a, b, *args, instructor="Colt", **kwargs):
    print(type(args))
    return [a, b, args, instructor, kwargs]

print(display_info(1, 2, 3, last_name="Steele", job="Instructor"))

