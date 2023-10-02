#NOTE: look at python doc and then oveeride once you know how the sepcial method works or gets called
class DrumpyDict(dict):
    def __repr__(self):
        print("NONE OF YOUR BUSINESS")
        return super().__repr__()

    def __missing__(self, key):
        print(f"YOU WANT {key}? WELL IT AINT HERE!")
        
    def __setitem__(self, key, value):
        print("YOU WANT TOT CHANGE THE DICTIONARY?")
        print("OK FINE...")
        super().__setitem__(key, value) #updates the dictionary
        
    def __contains__(self, item):
        print("NO IT AINT HERE!")
        return False

data = DrumpyDict({'first':'Tom','animal':'cat'})
print(data)
data['city'] = "tokyo"
print(data)
'city'in data

