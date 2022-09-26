from itertools import count

class Tabla:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
           cls._instance = super(Tabla, cls).__new__(cls)
        return cls._instance

    diccionario = [{
        "nombreVariable":"",
        "variable":""
    }]

    def buscarId(self,id):
        for i in count(self.diccionario):
            if(self.diccionario[-i].nombreVariable == id.nombre):
                return True    
        return False

    def addContexto(self):
        self.diccionario.append({
        "nombreVariable":"",
        "variable":""
    })

    def delContexto(self):
        self.diccionario.pop()

    def addId(self,nombre,variable):
        self.diccionario[-1].nombreVariable = nombre
        self.diccionario[-1].variable = variable




class Id:
    nombre =""
    tipo =""
    inicializada = False
    usada = False


class Variable(Id):
    pass

class Funcion(Id):
    nombresVariables = []
