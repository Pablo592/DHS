from itertools import count

class Tabla:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
           cls._instance = super(Tabla, cls).__new__(cls)
        return cls._instance

    diccionario = [dict()]

    def buscarId(self,nombre):

        for i in range(0,len(self.diccionario)):
         if(("nombre-"+str(nombre)) in self.diccionario[-i]):
            return i, self.diccionario[-i].get("variable-"+str(nombre))
        return i, False

    def addContexto(self):
        self.diccionario.append(dict())

    def delContexto(self):
        self.diccionario.pop()

    def updateId(self,nombre,variable,i):
        if(nombre != None):
            self.diccionario[-i]["nombre-"+str(nombre)] = nombre
            self.diccionario[-i]["variable-"+str(nombre)] = variable

    def addId(self,nombre,variable):
        if(nombre != None):
            self.diccionario[-1]["nombre-"+str(nombre)] = nombre
            self.diccionario[-1]["variable-"+str(nombre)] = variable




class Id:

    nombre =""
    tipo =""
    inicializada = False
    usada = False

    def toJson(self):
        diccionario = dict()
        diccionario['nombre'] = self.nombre
        diccionario['tipo'] = self.tipo
        diccionario['inicializada'] = self.inicializada
        diccionario['usada'] = self.usada
        return diccionario

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

    def getTipoVariable(self):
        return 'variable'

class Funcion(Id):

    argumentos = []

    def addArg(self,nombre,tipo):
        self.argumentos.append(dict())
        self.argumentos[-1]["tipo"] = tipo
        self.argumentos[-1]["nombre"] = nombre

    def getArgumentos(self):
        return self.argumentos
        
    def setArgumentos(self,arg):
        self.argumentos = arg

    def resetArgumentos(self):
        self.argumentos = []

    def setNombre(self,nombre):   
        self.nombre = nombre

    def getTipoVariable(self):
        return 'funcion'

    def toJson(self):
        diccionario = dict()
        diccionario['nombre'] = self.nombre
        diccionario['tipo'] = self.tipo
        diccionario['inicializada'] = self.inicializada
        diccionario['usada'] = self.usada
        diccionario['argumentos'] = self.argumentos
        return diccionario