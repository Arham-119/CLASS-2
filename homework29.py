class BMW:
    def fuel_type(self):
        print("Fuel type: Petrol")

    def max_speed(self):
        print("Max speed: 250 km/h")


class Ferrari:
    def fuel_type(self):
        print("Fuel type: Petrol")

    def max_speed(self):
        print("Max speed: 340 km/h")


# Polymorphism: the same method calls work on different classes
for car in (BMW(), Ferrari()):
    car.fuel_type()
    car.max_speed()