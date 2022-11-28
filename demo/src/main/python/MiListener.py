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
    f.write("Tipo\t")
    f.write("Nombre\t")
    f.write("Inicializada\t")
    f.write("Usada\t")
    f.write("Argumentos de la funcion\t")
    f.write("\n")
    f.write("-------------------------------------------------------------------\n")
    f.write("\n")    

    tabla = Tabla()
    contexto = 0
    
    # Exit a parse tree produced by compiladoresParser#itop.
    def exitItop(self, ctx:compiladoresParser.ItopContext):
      #  print ("Term tiene " + str(ctx.getChildCount()) + " hijos")
      #  print ("Term -> text |" + ctx.getText() + "|")
       pass


    # Enter a parse tree produced by compiladoresParser#oparit.
    def enterOparit(self, ctx:compiladoresParser.OparitContext):
        pass

    # Exit a parse tree produced by compiladoresParser#oparit.
    def exitOparit(self, ctx:compiladoresParser.OparitContext):
        pass


    # Enter a parse tree produced by compiladoresParser#expo.
    def enterExpo(self, ctx:compiladoresParser.ExpoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#expo.
    def exitExpo(self, ctx:compiladoresParser.ExpoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#coma.
    def enterComa(self, ctx:compiladoresParser.ComaContext):
        pass

    # Exit a parse tree produced by compiladoresParser#coma.
    def exitComa(self, ctx:compiladoresParser.ComaContext):
        pass


    # Enter a parse tree produced by compiladoresParser#tie.
    def enterTie(self, ctx:compiladoresParser.TieContext):
        pass

    # Exit a parse tree produced by compiladoresParser#tie.
    def exitTie(self, ctx:compiladoresParser.TieContext):
        pass


    # Enter a parse tree produced by compiladoresParser#igualOperaciones.
    def enterIgualOperaciones(self, ctx:compiladoresParser.IgualOperacionesContext):
        pass

    # Exit a parse tree produced by compiladoresParser#igualOperaciones.
    def exitIgualOperaciones(self, ctx:compiladoresParser.IgualOperacionesContext):
        pass


    # Enter a parse tree produced by compiladoresParser#to.
    def enterTo(self, ctx:compiladoresParser.ToContext):
        pass

    # Exit a parse tree produced by compiladoresParser#to.
    def exitTo(self, ctx:compiladoresParser.ToContext):
        pass


    # Enter a parse tree produced by compiladoresParser#orLogico.
    def enterOrLogico(self, ctx:compiladoresParser.OrLogicoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#orLogico.
    def exitOrLogico(self, ctx:compiladoresParser.OrLogicoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#ti.
    def enterTi(self, ctx:compiladoresParser.TiContext):
        pass

    # Exit a parse tree produced by compiladoresParser#ti.
    def exitTi(self, ctx:compiladoresParser.TiContext):
        pass


    # Enter a parse tree produced by compiladoresParser#andLogico.
    def enterAndLogico(self, ctx:compiladoresParser.AndLogicoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#andLogico.
    def exitAndLogico(self, ctx:compiladoresParser.AndLogicoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#te.
    def enterTe(self, ctx:compiladoresParser.TeContext):
        pass

    # Exit a parse tree produced by compiladoresParser#te.
    def exitTe(self, ctx:compiladoresParser.TeContext):
        pass


    # Enter a parse tree produced by compiladoresParser#igualo.
    def enterIgualo(self, ctx:compiladoresParser.IgualoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#igualo.
    def exitIgualo(self, ctx:compiladoresParser.IgualoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#po.
    def enterPo(self, ctx:compiladoresParser.PoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#po.
    def exitPo(self, ctx:compiladoresParser.PoContext):
        pass

    # Enter a parse tree produced by compiladoresParser#pi.
    def enterPi(self, ctx:compiladoresParser.PiContext):
        pass

    # Exit a parse tree produced by compiladoresParser#pi.
    def exitPi(self, ctx:compiladoresParser.PiContext):
        pass


    # Enter a parse tree produced by compiladoresParser#termino.
    def enterTermino(self, ctx:compiladoresParser.TerminoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#termino.
    def exitTermino(self, ctx:compiladoresParser.TerminoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#multiDivi.
    def enterMultiDivi(self, ctx:compiladoresParser.MultiDiviContext):
        pass

    # Exit a parse tree produced by compiladoresParser#multiDivi.
    def exitMultiDivi(self, ctx:compiladoresParser.MultiDiviContext):
        pass


    # Enter a parse tree produced by compiladoresParser#pe.
    def enterPe(self, ctx:compiladoresParser.PeContext):
        pass

    # Exit a parse tree produced by compiladoresParser#pe.
    def exitPe(self, ctx:compiladoresParser.PeContext):
        pass


    # Enter a parse tree produced by compiladoresParser#prefijo.
    def enterPrefijo(self, ctx:compiladoresParser.PrefijoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#prefijo.
    def exitPrefijo(self, ctx:compiladoresParser.PrefijoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#factor.
    def enterFactor(self, ctx:compiladoresParser.FactorContext):
        pass

    # Exit a parse tree produced by compiladoresParser#factor.
    def exitFactor(self, ctx:compiladoresParser.FactorContext):
        pass


    # Enter a parse tree produced by compiladoresParser#prog.
    def enterProg(self, ctx:compiladoresParser.ProgContext):
        pass

    # Exit a parse tree produced by compiladoresParser#prog.
    def exitProg(self, ctx:compiladoresParser.ProgContext):
        pass


    # Enter a parse tree produced by compiladoresParser#instrucciones.
    def enterInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        pass

    # Exit a parse tree produced by compiladoresParser#instrucciones.
    def exitInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        pass


    # Enter a parse tree produced by compiladoresParser#instruccion.
    def enterInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#instruccion.
    def exitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        pass

    # Enter a parse tree produced by compiladoresParser#bloque.
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
         self.f.write("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
         self.f.write("\t\t\t\tContexto: " + str(self.contexto)+"\n")
         self.f.write("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
         self.contexto +=1
         self.tabla.addContexto()
     #   print ("contenido llave: "+ctx.getText())

        

    # Exit a parse tree produced by compiladoresParser#bloque.
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
    #    self.f.write("\n")
    #    self.f.write(str(self.tabla.diccionario))
        print (self.tabla.diccionario)
        print ("\n")
        self.tabla.delContexto()
    #    self.f.write("\n")
    #    self.f.write(str(self.tabla.diccionario))

        if (len(self.tabla.diccionario) == 0 ):
            self.f.close()




    # Enter a parse tree produced by compiladoresParser#variable.
    def enterVariable(self, ctx:compiladoresParser.VariableContext):
        pass
        

    # Exit a parse tree produced by compiladoresParser#variable.
    def exitVariable(self, ctx:compiladoresParser.VariableContext):
        pass
    

    # Enter a parse tree produced by compiladoresParser#declaroAsigno.
    def enterDeclaroAsigno(self, ctx:compiladoresParser.DeclaroAsignoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#declaroAsigno.
    def exitDeclaroAsigno(self, ctx:compiladoresParser.DeclaroAsignoContext):
     #   print("Salgo exitDeclaroAsigno "+ctx.getText())

        variable = Variable()

        datos = ctx.getText()
        variable.setInicializada(True)

        if  datos.startswith("int"):
            variable.setTipo('int')
            datos = datos[3:]
        elif datos.startswith("string"):
            variable.setTipo('string')
            datos = datos[6:]
        elif datos.startswith("float"):
            variable.setTipo('float')
            datos = datos[5:]
        elif datos.startswith("double"):
            variable.setTipo('double')
            datos = datos[6:]
        elif datos.startswith("long"):
            variable.setTipo('long')
            datos = datos[4:]

        if "," in datos:
            dato = datos.split(",")

            for i in dato:
                
                if "*=" in i:
                    d = i.split("*=")
                elif "/=" in i:
                    d = i.split("/=")
                elif "%=" in i:
                    d = i.split("%=")
                elif "+=" in i:
                    d = i.split("+=")
                elif "-=" in i:
                    d = i.split("-=")
                else:
                    d = i.split("=")
                v = variable.clone()
                v.setNombre(d[0])
                if(len(d)> 1):
                   resul = self.existeVariable(d[0],v.toJson(),'creoInicializo')
                   if resul:
                       self.f.write(v.getTipo())
                       self.f.write("\t\t")
                       self.f.write(v.getNombre())
                       if len(v.getNombre()) > 1:                                     
                        self.f.write("\t")
                       else:
                        self.f.write("\t\t")
                       self.f.write(str(v.getInicializada()))
                       self.f.write("\t\t\t")
                       self.f.write(str(v.getUsada()))
                       self.f.write("\n")
                else:
                   resul = self.existeVariable(d[0],v.toJson(),'creo')
                   if resul:
                       self.f.write(v.getTipo())
                       self.f.write("\t\t")
                       self.f.write(v.getNombre())
                       if len(v.getNombre()) > 1:                                     
                        self.f.write("\t")
                       else:
                        self.f.write("\t\t")
                       self.f.write(str(v.getInicializada()))
                       self.f.write("\t\t\t")
                       self.f.write(str(v.getUsada()))
                       self.f.write("\n")
        else:

            if "*=" in datos:
               d = datos.split("*=")
            elif "/=" in datos:
               d = datos.split("/=")
            elif "%=" in datos:
               d = datos.split("%=")
            elif "+=" in datos:
               d = datos.split("+=")
            elif "-=" in datos:
               d = datos.split("-=")
            else:
               d = datos.split("=")
            v = variable.clone()
            v.setNombre(d[0])
            resul = self.existeVariable(d[0],v.toJson(),'creoInicializo')
            if resul:
                       self.f.write(v.getTipo())
                       self.f.write("\t\t")
                       self.f.write(v.getNombre())
                       if len(v.getNombre()) > 1:                                     
                        self.f.write("\t")
                       else:
                        self.f.write("\t\t")
                       self.f.write(str(v.getInicializada()))
                       self.f.write("\t\t\t")
                       self.f.write(str(v.getUsada()))
                       self.f.write("\n")

    # Enter a parse tree produced by compiladoresParser#asignacion.
    def enterAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#asignacion.
    def exitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
     #   print("Salgo exitAsignacion "+ctx.getText())
        variable = Variable()
        variable.setUsada(True)
        datos = ctx.getText()
        if "*=" in datos:
               d = datos.split("*=")
        elif "/=" in datos:
            d = datos.split("/=")
        elif "%=" in datos:
            d = datos.split("%=")
        elif "+=" in datos:
            d = datos.split("+=")
        elif "-=" in datos:
            d = datos.split("-=")
        else:
            d = datos.split("=")
        v = variable.clone()
        v.setNombre(d[0])
        if(len(d)> 1):
            resul = self.existeVariable(d[0],v.toJson(),'uso')
            if resul:
                       self.f.write(v.getTipo())
                       self.f.write("\t\t")
                       self.f.write(v.getNombre())
                       if len(v.getNombre()) > 1:                                     
                        self.f.write("\t")
                       else:
                        self.f.write("\t\t")
                       self.f.write("True")
                       self.f.write("\t\t\t")
                       self.f.write("True")
                       self.f.write("\n")
            valor = d[1]
            posiblesVariables = []

         
            aux1 = valor.split('+')
            for i in aux1:
             aux2 = i.split('-')
             for j in aux2:
              aux3 = j.split('*')
              for k in aux3:
                aux4 = k.split('/')
                for m in aux4:
                 if(not m.isnumeric()):
                    if(m != ""):
                     posiblesVariables.append(m)
            
            for i  in posiblesVariables:
              if(("(" in i) & (")" not in i)):
                i = i[1:]

              if(("(" not in i) & (")" in i)):
                i = i[0:-1]

              if(i.isnumeric()):
                continue

              resul = self.existeVariable(i,"algo",'uso')
              if resul:
                       self.f.write(v.getTipo())
                       self.f.write("\t\t")
                       self.f.write(v.getNombre())
                       if len(v.getNombre()) > 1:                                     
                        self.f.write("\t")
                       else:
                        self.f.write("\t\t")
                       self.f.write("True")
                       self.f.write("\t\t\t")
                       self.f.write("True")
                       self.f.write("\n")


    # Enter a parse tree produced by compiladoresParser#prototipadoFuncion.
    def enterPrototipadoFuncion(self, ctx:compiladoresParser.PrototipadoFuncionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#prototipadoFuncion.
    def exitPrototipadoFuncion(self, ctx:compiladoresParser.PrototipadoFuncionContext):
        funcion = Funcion()
        datos = ctx.getText()
        funcion.setInicializada(True)

        if  datos.startswith("int"):
            funcion.setTipo('int')
            datos = datos[3:]
        elif datos.startswith("string"):
            funcion.setTipo('string')
            datos = datos[6:]
        elif datos.startswith("float"):
            funcion.setTipo('float')
            datos = datos[5:]
        elif datos.startswith("double"):
            funcion.setTipo('double')
            datos = datos[6:]
        elif datos.startswith("long"):
            funcion.setTipo('long')
            datos = datos[4:]

        datos = datos.split('(')
        funcion.setNombre(datos[0])
        nomFun = datos[0]

        datos = datos[1].split(')')[0]

        if "," in datos:
            dato = datos.split(",")
            tipo = ""
            for i in dato:
                if "int" in i:
                  tipo ='int'
                  nombre = i[3:]
                elif "string" in i:
                  tipo ='string'
                  nombre = i[6:]
                elif "float" in i:
                  tipo ='float'
                  nombre = i[5:]
                elif "double" in i:
                  tipo ='double'
                  nombre = i[6:]
                elif "long" in i:
                  tipo ='long'
                  nombre = i[4:]
                else:
                  nombre = i
                funcion.addArg(nombre,tipo)

        print(funcion.getArgumentos())
                
        resul = self.existeVariable(funcion.getNombre(),funcion.toJson(),'creo')
        if resul:
                    self.f.write(funcion.getTipo())
                    self.f.write("\t\t")
                    self.f.write(funcion.getNombre())
                    if len(funcion.getNombre()) > 1:                                     
                        self.f.write("\t")
                    else:
                       self.f.write("\t\t")
                       self.f.write(str(funcion.getInicializada()))
                       self.f.write("\t\t\t")
                       self.f.write(str(funcion.getUsada()))
                       self.f.write("\t")
                    for i in funcion.getArgumentos():
                        self.f.write(i['tipo'])
                        self.f.write("\t\t")
                        self.f.write(i['nombre'])
                        self.f.write("\t\t")
                    self.f.write("\n")


    # Enter a parse tree produced by compiladoresParser#llamadoAFunciones.
    def enterLlamadoAFunciones(self, ctx:compiladoresParser.LlamadoAFuncionesContext):
        pass

    # Exit a parse tree produced by compiladoresParser#llamadoAFunciones.
    def exitLlamadoAFunciones(self, ctx:compiladoresParser.LlamadoAFuncionesContext):
        pass


    # Enter a parse tree produced by compiladoresParser#desarrolloFuncion.
    def enterDesarrolloFuncion(self, ctx:compiladoresParser.DesarrolloFuncionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#desarrolloFuncion.
    def exitDesarrolloFuncion(self, ctx:compiladoresParser.DesarrolloFuncionContext):
        pass

    # Enter a parse tree produced by compiladoresParser#retorno.
    def enterRetorno(self, ctx:compiladoresParser.RetornoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#retorno.
    def exitRetorno(self, ctx:compiladoresParser.RetornoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloqueif.
    def enterBloqueif(self, ctx:compiladoresParser.BloqueifContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloqueif.
    def exitBloqueif(self, ctx:compiladoresParser.BloqueifContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloquewhile.
    def enterBloquewhile(self, ctx:compiladoresParser.BloquewhileContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloquewhile.
    def exitBloquewhile(self, ctx:compiladoresParser.BloquewhileContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloquefor.
    def enterBloquefor(self, ctx:compiladoresParser.BloqueforContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloquefor.
    def exitBloquefor(self, ctx:compiladoresParser.BloqueforContext):
        pass



    def existeVariable(self,nombre,variable,caso):
        i ,resultado = self.tabla.buscarId(nombre)

        if(resultado == False):
            if(str(caso) == 'uso'):
                if ("(" in nombre):
                    self.existeVariable(nombre.split("(")[0],variable,caso)
                else:
                    print("Error, la variable \""+str(nombre)+"\" no existe")
            if(str(caso) == 'creoInicializo'):
                self.tabla.addId(str(nombre),variable)
                return True
            if(str(caso) == 'creo'):
                self.tabla.addId(str(nombre),variable)
                return True
        else:
            if(str(caso) == 'uso'):
             resultado['usada'] = True
             self.tabla.addIdi(str(nombre),resultado,i)
             return True
            else:
             print("Error, la variable "+str(nombre)+" ya se encuentra creada")

del compiladoresParser