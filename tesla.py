from vehicle import Vehicle

class Tesla(Vehicle):

    def __init__(self, color, occupancy):
        super().__init__(color, occupancy)

    def drive(self):
        print(f"Time to go on a joy ride in the {self.color} Tesla!")