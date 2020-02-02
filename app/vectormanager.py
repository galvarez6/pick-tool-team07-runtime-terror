from models.vector import Vector

class VectorManager: 
    __instance = None

    def __init__(self):
        if VectorManager.__instance == None: 
            VectorManager.__instance = self
            self.vectors = []
        else: 
            raise Exception("Trying to create another instance of a singelton class") 
    
    @staticmethod
    def get_instance(): 
        if VectorManager.__instance == None: 
            VectorManager()
        return VectorManager.__instance

    def add_vector(self, name, desc): 
        v = Vector()
        v.setName(name)
        v.setDescription(desc)
        self.vectors.append(v)

    def get_vectors(self): 
        return self.vectors