from ride import Ride, RideRequest, RideMatching, RideSharing
from users import Rider, Driver
from vehicle import Car, Bike

neffroxx = RideSharing('neffroxx')

karim = Rider("Karim Uddin", "karim@gmail.com", 1234, "Cumilla", 1200)
neffroxx.add_rider(karim)

rahim = Driver("Rahim Uddin", "rahim@gmail.com", 1256, "Gulshan")
neffroxx.add_driver(rahim)

