class Vector(object):
    def __init__(self):
        self.name = None
        self.description = None
        self.startdatetime = None
        self.enddatetime = None

    def setName(self, name):
        self.name = name

    def setDescription(self, desc):
        self.description = desc