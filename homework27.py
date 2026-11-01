class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100


class Bus(Vehicle):
    def fare(self):
        total_fare = super().fare()               # 50 * 100 = 5000
        return total_fare + (total_fare * 0.10)   # 5000 + 500 = 5500


bus = Bus(50)
print("Total bus fare is:", bus.fare())