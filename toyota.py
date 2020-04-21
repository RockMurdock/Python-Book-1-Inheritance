from vehicle import Vehicle

class Toyota(Vehicle):

    def __init__(self, color, occupancy):
        super().__init__(color, occupancy)

    def drive(self):
        print(f"Time to go on a joy ride in the {self.color} Toyota!")

    def turn(self, direction):
        print(f"The Toyota turns {direction} down Main Street!")

    def stop(self):
        print("The Toyota comes to a complete stop")