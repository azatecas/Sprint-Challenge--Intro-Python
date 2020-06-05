# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

#base class for flightVehicle and Ground vehicle
class Vehicle:
    pass

#Base Class for Starship and Airplane
class Flight_Vehicle(Vehicle):
    def __init__(self):
        super().__init__()
        pass

#base class for Car and Motorcycle
class Ground_Vehicle(Vehicle):
    def __init__(self):
        super().__init__()
        pass

class Airplane(Flight_Vehicle):
    def __init__(self):
        super().__init__()
        pass

class Starship(Flight_Vehicle):
    def __init__(self):
        super().__init__()
        pass

class Car(Ground_Vehicle):
    def __init__(self):
        super().__init__()
        pass

