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
        v = Vector(name, desc)
        self.vectors.append(v)

    def vector_exists(self, name): 
        for vector in self.vectors: 
            if vector.name == name: 
                return True
        return False

    def get_vectors(self): 
        return self.vectors

    def update_vector(self, vector, name, desc): 
        for vector in self.vectors: 
            if vector.name == vector: 
                vector.name, vector.description = name, desc