
class EventConfig(object): 
    def __init__(self):
        self.name = None 
        self.desc = None
        self.start = None 
        self.end = None
        self.rootDir = None    
        self.redFolder = None 
        self.blueFolder = None
        self.whiteFolder = None
        self.lead = None 
        self.leadIp = None 
        self.connections = None 
    
    def setName(self, name):
        self.name = name

    def setDesc(self, desc): 
        self.desc = desc

    def setStart(self, start): 
        self.start = start

    def setEnd(self, end): 
        self.end = end

    def setRootDir(self, rootDir): 
        self.rootDir = rootDir

    def setRed(self, red):
        self.redFolder = red

    def setBlue(self, blue): 
        self.blueFolder = blue

    def setWhite(self, white):
        self.whiteFolder = white

    def setLead(self, lead): 
        self.lead = lead

    def setLeadIp(self, ip):
        self.leadIp = ip

    def setConnections(self, conn):
        self.connections = conn     
    
    def getName(self):
        return self.name 

    def setDesc(self): 
        return self.desc

    def setStart(self): 
        return self.start

    def setEnd(self): 
        return self.end

    def setRootDir(self): 
        return self.rootDir

    def setRed(self):
        return self.redFolder 

    def setBlue(self): 
        return self.blueFolder

    def setWhite(self):
        return self.whiteFolder

    def setLead(self): 
        return self.lead

    def setLeadIp(self):
        return self.leadIp

    def setConnections(self, conn):
        self.connections = conn     
    

    
