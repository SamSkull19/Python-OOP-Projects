from abc import ABC

class Vehicle(ABC):
    speed = {
        'car' : 50,
        'bike' : 20,
        'cng' : 30,
    }

    def __init__(self, vehicle_type, license_plate, rate):
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate = rate

