class Parrot:
    # instance attributes
 def __init__(self, name, age):
        self.name = name
        self.age = age
    # instance method
 def sing(self, song):
        return "{} is singing".format(self.name, song)
 def dance(self):
        return "{} is dancing".format(self.name)
 def dance(self):
        return "{} is now dancing" . format(self.name)
 # instantiate the object
 blu= parrot ("Blu", 10)

#call our instance methods
print (Blu.sing("'Happy'"))
print (Blu.dance())
 

