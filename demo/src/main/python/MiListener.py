# Generated from /home/pablo/Escritorio/Repositorios/DHS-Cursado/demo/src/main/python/compiladores.g4 by ANTLR 4.9.2
from itertools import count
from pickle import TRUE
from antlr4 import *

from clases import Tabla
from clases import Variable
from clases import Funcion

from compiladoresParser import compiladoresParser

# This class defines a complete listener for a parse tree produced by compiladoresParser.
class MiListener(ParseTreeListener):


    f = open("output/Tabla_De_Simbolos.txt", "w")
     


    variables = [dict()]
    tabla = Tabla()
    contexto = 0
    tipoDato = ""
    

  # Enter a parse tree produced by compiladoresParser#itop.
    def enterItop(self, ctx:compiladoresParser.ItopContext):
        pass

    # Exit a parse tree produced by compiladoresParser#itop.
    def exitItop(self, ctx:compiladoresParser.ItopContext):
        datos = ctx.getText()
        if(datos != ""):
            for i in self.tabla.diccionario:
                i.items()
 
            print(str(datos) + "--> exitItop")
            print("\n")  


            if(not(("," in datos) & ("(" in datos))):
                for i in range(0,len(self.variables)-1):
                    id = Variable()
                    id.setInicializada(True)
                    id.setNombre(self.variables[i].get('nombre'))
                    id.setTipo(self.variables[i].get('tdato'))

                    if(id.getNombre() == None):
                        continue
                    m, respuesta = self.tabla.buscarId(id.getNombre())


                    if(respuesta == False):
                        self.tabla.addId(id.getNombre(),id)
                    elif(respuesta.getTipoVariable() != 'funcion'):
                        self.tabla.updateId(id.getNombre(),respuesta,m)                  

                    del id
            
            for i in self.tabla.diccionario:
                i.items()
            self.variables = [dict()]
            self.tipoDato = ""
     


    # Enter a parse tree produced by compiladoresParser#oparit.
    def enterOparit(self, ctx:compiladoresParser.OparitContext):
        pass

    # Exit a parse tree produced by compiladoresParser#oparit.
    def exitOparit(self, ctx:compiladoresParser.OparitContext):
        pass

    # Enter a parse tree produced by compiladoresParser#bloque.
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):


         print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
         print("\t\t\t\tContexto: " + str(self.contexto)+"\n")
         print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")

         self.tabla.addContexto()

    # Exit a parse tree produced by compiladoresParser#bloque.
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):

        self.f.write("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
        self.f.write("\t\t\t\t\t\t\tContexto: " + str(self.contexto)+"\n")
        self.f.write("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
        self.f.write("Tipo\t")
        self.f.write("Nombre\t")
        self.f.write("Inicializada\t")
        self.f.write("Usada\t")
        self.f.write("Argumentos de la funcion\t")
        self.f.write("\n")
        self.f.write("-------------------------------------------------------------------\n")
        self.f.write("\n")   

        self.contexto +=1

        for hoja in self.tabla.diccionario:
            self.f.write("{\n\n")
            for key ,value in hoja.items():

                if("variable-" in key):
                    self.f.write(value.getTipo())
                    self.f.write("\t\t")
                    self.f.write(value.getNombre())
                    if(len(value.getNombre())> 1):
                        self.f.write("\t\t")
                    else:
                        self.f.write("\t\t\t")
                    self.f.write(str(value.getInicializada()))
                    self.f.write("\t\t")
                    self.f.write(str(value.getUsada()))
                    self.f.write("\t\t")
                    if(value.getTipoVariable() == 'funcion'):
                        for i in value.getArgumentos():
                            self.f.write(i.get("tipo"))
                            self.f.write("\t\t")
                            self.f.write(i.get("nombre"))
                            self.f.write("\t\t")
                        self.f.write("\n")
                    else:
                        self.f.write("\n")
            self.f.write("}\n")

        self.variables = [dict()]
        self.tipoDato = ""
        self.tabla.delContexto()


    # Enter a parse tree produced by compiladoresParser#expo.
    def enterExpo(self, ctx:compiladoresParser.ExpoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#expo.
    def exitExpo(self, ctx:compiladoresParser.ExpoContext):
        pass

    # Enter a parse tree produced by compiladoresParser#variable.
    def enterVariable(self, ctx:compiladoresParser.VariableContext):
        pass

    # Exit a parse tree produced by compiladoresParser#variable.
    def exitVariable(self, ctx:compiladoresParser.VariableContext):
        datos = ctx.getText()
        if(datos != ""):
 
            print(str(datos) + "--> exitVariable")
            print("\n")


            if(datos == 'main'):
                self.variables = [dict()]
                self.tipoDato = ""

            else:
                if(self.tipoDato == ""):
                    i, respuesta = self.tabla.buscarId(datos)
                    if(respuesta == False):
                        self.f.write("***** La variable " + "\"" + str(datos) + "\"" + " no se encuentra declarada ***** \n")
                        return
                    else:
                        respuesta.setUsada(True)
                        self.tabla.updateId(datos,respuesta,i)
                        self.variables[-1]['tdato'] = respuesta.getTipo()
                        self.variables[-1]['nombre'] = datos
                        self.variables.append(dict())
                        del respuesta
                else:
                    self.variables[-1]['tdato'] = self.tipoDato
                    self.variables[-1]['nombre'] = datos
                    self.variables.append(dict())
        for i in self.tabla.diccionario:
                i.items()

     # Enter a parse tree produced by compiladoresParser#tdato.
    def enterTdato(self, ctx:compiladoresParser.TdatoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#tdato.
    def exitTdato(self, ctx:compiladoresParser.TdatoContext):
        datos = ctx.getText()
        if(datos != ""):

            print(str(datos) + "--> exitTdato")
            print("\n")

            self.tipoDato = datos



     # Enter a parse tree produced by compiladoresParser#numero.
    def enterNumero(self, ctx:compiladoresParser.NumeroContext):
        pass

    # Exit a parse tree produced by compiladoresParser#numero.
    def exitNumero(self, ctx:compiladoresParser.NumeroContext):
        datos = ctx.getText()
        if(datos != ""):
   
            print(str(datos) + "--> exitNumero")
            print("\n")
  

    # Enter a parse tree produced by compiladoresParser#declaroAsigno.
    def enterDeclaroAsigno(self, ctx:compiladoresParser.DeclaroAsignoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#declaroAsigno.
    def exitDeclaroAsigno(self, ctx:compiladoresParser.DeclaroAsignoContext):
        pass

    # Enter a parse tree produced by compiladoresParser#asignacion.
    def enterAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        datos = ctx.getText()
        if(datos != ""):

            print(str(datos) + "--> enterAsignacion")
            self.f.write("\n")

    # Exit a parse tree produced by compiladoresParser#asignacion.
    def exitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#prototipadoFuncion.
    def enterPrototipadoFuncion(self, ctx:compiladoresParser.PrototipadoFuncionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#prototipadoFuncion.
    def exitPrototipadoFuncion(self, ctx:compiladoresParser.PrototipadoFuncionContext):
        datos = ctx.getText()
        if(datos != ""):

            print(str(datos) + "--> exitPrototipadoFuncion")
            print("\n")

            funcion = Funcion()

            funcion.setNombre(self.variables[0].get('nombre'))
            funcion.resetArgumentos()
            funcion.setTipo(self.variables[0].get('tdato'))
            funcion.setInicializada(True)

            for i in range(1,len(self.variables)-1):
                funcion.addArg(self.variables[i]['nombre'], self.variables[i]['tdato'])

            self.tabla.addId(funcion.getNombre(),funcion)

            self.variables = [dict()]
            self.tipoDato = ""
            for i in self.tabla.diccionario:
                i.items()

            del funcion

    # Enter a parse tree produced by compiladoresParser#llamadoAFunciones.
    def enterLlamadoAFunciones(self, ctx:compiladoresParser.LlamadoAFuncionesContext):
        pass

    # Exit a parse tree produced by compiladoresParser#llamadoAFunciones.
    def exitLlamadoAFunciones(self, ctx:compiladoresParser.LlamadoAFuncionesContext):
        datos = ctx.getText()
        if(datos != ""):
            for i in self.tabla.diccionario:
                i.items()

            print(str(datos) + "--> exitLlamadoAFunciones")
            print("\n")
   
            nombreFuncion = datos.split("(")[0]    
            print(nombreFuncion)

            for t in range(0,len(self.variables)-1):
                if(nombreFuncion == self.variables[t]['nombre']):
                    index = t

            m, respuesta = self.tabla.buscarId(nombreFuncion)

            if(respuesta == False):
                self.f.write("***** La funcion \"" + str(nombreFuncion) + "\" no se encuentra declarada *****\n")
                return
            else:
                if(respuesta.getTipoVariable() == "variable"):
                        self.f.write("***** \"" + str(respuesta.getNombre()) + "\" no es una funcion *****\n")
                        return
                respuesta.resetArgumentos()
                for i in range(index + 1,len(self.variables)-1):
                    if(self.variables[i]['nombre'] != None):
                        j, vari = self.tabla.buscarId(self.variables[i]['nombre'])
                
                    respuesta.addArg(self.variables[i].get('nombre'), vari.getTipo())
                self.tabla.updateId(nombreFuncion,respuesta,m)

              
            for i in self.tabla.diccionario:
                i.items()
            self.variables = [dict()]
            self.tipoDato = ""
     



    # Enter a parse tree produced by compiladoresParser#desarrolloFuncion.
    def enterDesarrolloFuncion(self, ctx:compiladoresParser.DesarrolloFuncionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#desarrolloFuncion.
    def exitDesarrolloFuncion(self, ctx:compiladoresParser.DesarrolloFuncionContext):
        pass


del compiladoresParser