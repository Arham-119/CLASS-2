class Dog:
    # Class variable
    animal = "Mammal"

    # Constructor with instance variables
    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour


# Creating two different objects for different breeds of dogs
dog1 = Dog("Golden Retriever", "Golden")
dog2 = Dog("German Shepherd", "Black and Tan")

# Displaying the details of both breeds of dogs
print("Dog 1 Details:")
print(f"Animal Type: {Dog.animal}")
print(f"Breed: {dog1.breed}")
print(f"Colour: {dog1.colour}\n")

print("Dog 2 Details:")
print(f"Animal Type: {Dog.animal}")
print(f"Breed: {dog2.breed}")
print(f"Colour: {dog2.colour}")