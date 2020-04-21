from vehicle import Vehicle
from subaru import Subaru
from honda import Honda
from tesla import Tesla
from toyota import Toyota
from nissan import Nissan

"""
Define 5 of your favorite vehicles
Move all common properties in your vehicles to a new Vehicle class.
Create an instance of each vehicle.
Define a different value for each vehicle's properties.
Create a drive() method in the Vehicle class.
Override the drive() method in all the other vehicle classes. Include the vehicle's color in the message (i.e. "The blue Ram drives past. RRrrrrrummbbble!").
Create a turn(self, direction) method, and a stop(self) method on Vehicle. Define a basic implementation of each.
Override all three of those methods on some of the vehicles. For example, the stop() method for a plane would be to output the message "The white Cessna rolls to a stop after rolling a mile down the runway."
Make your vehicle instances perform all three behaviors.
"""

subaru = Subaru("blue", 5)
honda = Honda("red", 5)
tesla = Tesla("silver", 5)
toyota = Toyota("green", 5)
nissan = Nissan("black", 5)

subaru.drive()
subaru.turn("left")
subaru.stop()

honda.drive()
honda.turn("right")
honda.stop()

tesla.drive()
tesla.turn("left")
tesla.stop()

toyota.drive()
toyota.turn("left")
toyota.stop()

nissan.drive()
nissan.turn("right")
nissan.stop()
