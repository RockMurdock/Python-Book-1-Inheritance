from vehicle import Vehicle

class Subaru(Vehicle):

    def __init__(self, color, occupancy):
        super().__init__(color, occupancy)

    def drive(self):
        print(f"Time to go on a joy ride in the {self.color} Subaru!")