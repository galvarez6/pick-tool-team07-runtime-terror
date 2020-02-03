from models.eventconfig import EventConfig

class EventConfigManager: 
    __instance = None

    def __init__(self):
        if EventConfigManager.__instance == None: 
            EventConfigManager.__instance = self
            self.eventconfig = None
        else: 
            raise Exception("Trying to create another instance of a singelton class") 
    
    @staticmethod
    def get_instance(): 
        if EventConfigManager.__instance == None: 
            EventConfigManager()
        return EventConfigManager.__instance

    def create_eventconfig(self, name, desc, start, end): 
        self.eventconfig = EventConfig(name, desc, start, end)

    def get_eventconfig(self): 
        return self.eventconfig