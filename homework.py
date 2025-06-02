class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self, sound):
        return f"{self.name} says {sound}"

# Create objects
dog = Animal("Buddy", "Dog")
cat = Animal("Whiskers", "Cat")

# Call methods
print(dog.speak("Woof!"))
print(cat.speak("Meow!"))