from itertools import count

class Tabla:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
           cls._instance = super(Tabla, cls).__new__(cls)
        return cls._instance

    diccionario = [dict()]

    def buscarId(self,id):
        for i in count(self.diccionario):
            if(self.diccionario[-i].nombreVariable == id.nombre):
                return True    
        return False

    def addContexto(self):
        self.diccionario.append(dict())

    def delContexto(self):
        self.diccionario.pop()

    def addId(self,nombre,variable):
        self.diccionario[-1].get("nombreVariable")
        self.diccionario[-1]['nombreVariable'] = nombre
        self.diccionario[-1].get("variable")
        self.diccionario[-1]['variable'] = variable




class Id:

    nombre =""
    tipo =""
    inicializada = False
    usada = False

    def toString(self):
        return vars(self)

    def setNombre(self,nombre):
        self.nombre = nombre

    def setTipo(self,tipo):
        self.tipo = tipo

    def setInicializada(self,inicializada):
        self.inicializada = inicializada

    def setUsada(self,usada):
        self.usada = usada


    def getNombre(self):
        return self.nombre

    def getTipo(self):
        return self.tipo

    def getInicializada(self):
        return self.inicializada

    def getUsada(self):
        return self.usada

    def clone(self):
        id = Id()

        id.setInicializada(self.getInicializada())
        id.setNombre(self.getNombre())
        id.setTipo(self.getTipo())
        id.setUsada(self.getUsada())
        return id


class Variable(Id):
    pass

class Funcion(Id):
    nombresVariables = []
