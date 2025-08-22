class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teacher = {}   
        self.classroom = {} # { name : classroom object }

    