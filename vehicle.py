class Vehicle:

    def __init__(self, color, occupancy):
        self.color = color
        self.occupancy = occupancy

    def drive(self):
        print("VROOOOM")

    def turn(self, direction):
        print(f"The vehicle turns {direction}.")

    def stop(self):
        print(f"The vehicle has stopped.")