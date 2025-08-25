from datetime import datetime

class Ride:
    def __init__(self, start_location, end_location):
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_time = None

    def set_driver(self, driver):
        self.driver = driver

    def start_ride(self):
        self.start_time = datetime.now()    
        
    def end_ride(self):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_time
        self.driver.wallet += self.estimated_time

    def __repr__(self):
        return f'Ride Details : Started {self.start_time} to Ended {self.end_location}'