class Circle:
    # Constructor with a variable radius inside it
    def __init__(self, radius):
        self.radius = radius

    # Function to calculate and return the area
    def area(self):
        return 3.14159 * (self.radius ** 2)

    # Function to calculate and return the perimeter
    def perimeter(self):
        return 2 * 3.14159 * self.radius


# Taking input for the radius from the user
user_radius = float(input("Enter the radius of the circle: "))

# Creating an object of the Circle class
my_circle = Circle(user_radius)

# Displaying the results
print(f"Radius: {my_circle.radius}")
print(f"Area: {my_circle.area():.2f}")
print(f"Perimeter: {my_circle.perimeter():.2f}")