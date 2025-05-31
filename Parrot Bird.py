class Parrot :
    # class attribute
    species = "bird"
    # instance attributes
    def __init__(self, name, age):
        self.name =name
        self.age =age
        # intantiate the Parrot class
blu = Parrot ("Blu", 10)
woo = Parrot ("Woo", 15)

        # access the class attributes
print ("Blu is a {}".format (woo.species))
        # access the instance attributes
print ("{} is {} years old".format(blu.name, blu))
print ("{} is {} years old".format(woo.name, woo))