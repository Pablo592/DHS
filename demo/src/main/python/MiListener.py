# Generated from /home/pablo/Escritorio/Repositorios/DHS-Cursado/demo/src/main/python/compiladores.g4 by ANTLR 4.9.2
from itertools import count
from pickle import TRUE
from antlr4 import *

from clases import Tabla
from clases import Id


from compiladoresParser import compiladoresParser

# This class defines a complete listener for a parse tree produced by compiladoresParser.
class MiListener(ParseTreeListener):

    tabla = Tabla()
    
    # Exit a parse tree produced by compiladoresParser#itop.
    def exitItop(self, ctx:compiladoresParser.ItopContext):
        print ("Term tiene " + str(ctx.getChildCount()) + " hijos")
        print ("Term -> text |" + ctx.getText() + "|")


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


    # Enter a parse tree produced by compiladoresParser#relaciono.
    def enterRelaciono(self, ctx:compiladoresParser.RelacionoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#relaciono.
    def exitRelaciono(self, ctx:compiladoresParser.RelacionoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#pi.
    def enterPi(self, ctx:compiladoresParser.PiContext):
        pass

    # Exit a parse tree produced by compiladoresParser#pi.
    def exitPi(self, ctx:compiladoresParser.PiContext):
        pass


    # Enter a parse tree produced by compiladoresParser#t.
    def enterT(self, ctx:compiladoresParser.TContext):
        pass

    # Exit a parse tree produced by compiladoresParser#t.
    def exitT(self, ctx:compiladoresParser.TContext):
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
        self.tabla.addContexto()
        print ("contenido llave: "+ctx.getText())

        

    # Exit a parse tree produced by compiladoresParser#bloque.
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        print("\n")
        print (self.tabla.diccionario)
        print("\n")
        self.tabla.delContexto()
    #    print ("Term tiene " + str(ctx.getChildCount()) + " hijos")
    #    print ("Term -> text |" + ctx.getText() + "|")


   




    # Enter a parse tree produced by compiladoresParser#variable.
    def enterVariable(self, ctx:compiladoresParser.VariableContext):
        pass
        

    # Exit a parse tree produced by compiladoresParser#variable.
    def exitVariable(self, ctx:compiladoresParser.VariableContext):
        pass
       




    # Enter a parse tree produced by compiladoresParser#declaracion.
    def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        pass
    
    


    # Exit a parse tree produced by compiladoresParser#declaracion.
    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
      #   print("Salgo exitDeclaracion "+ctx.getText())
         variable = Id()

         datos = ctx.getText()
         variable.setInicializada(True)

         if "int" in datos:
            variable.setTipo('int')
            datos = datos[3:]
         elif "string" in datos:
            variable.setTipo('string')
            datos = datos[6:]
         elif "float" in datos:
            variable.setTipo('float')
            datos = datos[5:]
         elif "double" in datos:
            variable.setTipo('double')
            datos = datos[6:]
         elif "long" in datos:
            variable.setTipo('long')
            datos = datos[4:]

        # print(datos)

         if "," in datos:
            dato = datos.split(",")

            for i in dato:
                v = variable.clone()
                v.setNombre(i)
                self.existeVariable(i,v.toJson(),'creo')
                    

         else:
            v = variable.clone()
            v.setNombre(datos)
            self.existeVariable(datos,v.toJson(),'creo')
         #   print("d+-d+-d+-d+-d+-d+-d+-d+-d+-d+-d+-d+d-")
         #   print(d)
         #   print(v.toJson())

    # Enter a parse tree produced by compiladoresParser#declaroAsigno.
    def enterDeclaroAsigno(self, ctx:compiladoresParser.DeclaroAsignoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#declaroAsigno.
    def exitDeclaroAsigno(self, ctx:compiladoresParser.DeclaroAsignoContext):
     #   print("Salgo exitDeclaroAsigno "+ctx.getText())

        variable = Id()

        datos = ctx.getText()
        variable.setInicializada(True)

        if "int" in datos:
            variable.setTipo('int')
            datos = datos[3:]
        elif "string" in datos:
            variable.setTipo('string')
            datos = datos[6:]
        elif "float" in datos:
            variable.setTipo('float')
            datos = datos[5:]
        elif "double" in datos:
            variable.setTipo('double')
            datos = datos[6:]
        elif "long" in datos:
            variable.setTipo('long')
            datos = datos[4:]

        if "," in datos:
            dato = datos.split(",")

            for i in dato:
                d = i.split("=")
                v = variable.clone()
                v.setNombre(d[0])
                if(len(d)> 1):
                    self.existeVariable(d[0],v.toJson(),'creoInicializo')
            #        print("d+-d+-d+-d+-d+-d+-d+-d+-d+-d+-d+-d+d-")
            #        print(d[1])
            #        print(v.toJson())
                else:
                    self.existeVariable(d[0],v.toJson(),'creo')
             #       print("d+-d+-d+-d+-d+-d+-d+-d+-d+-d+-d+-d+d-")
             #       print(v.toJson())
        else:
            d = datos.split("=")
            v = variable.clone()
            v.setNombre(d[0])
            self.existeVariable(d[0],v.toJson(),'creoInicializo')

            #self.tabla.addId(d[0],v.toJson())
         #   print("d+-d+-d+-d+-d+-d+-d+-d+-d+-d+-d+-d+d-")
         #   print(d[1])
         #   print(v.toJson())

    # Enter a parse tree produced by compiladoresParser#asignacion.
    def enterAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#asignacion.
    def exitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
     #   print("Salgo exitAsignacion "+ctx.getText())
        variable = Id()
        variable.setUsada(True)
        datos = ctx.getText()
        d = datos.split("=")
        v = variable.clone()
        v.setNombre(d[0])
        if(len(d)> 1):
            self.existeVariable(d[0],v.toJson(),'uso')
         #   self.tabla.addId(d[0],v.toJson())
         #   print("d+-d+-d+-d+-d+-d+-d+-d+-d+-d+-d+-d+d-")
        #    print(d[1])
         #   print(v.toJson())


    # Enter a parse tree produced by compiladoresParser#prototipadoFuncion.
    def enterPrototipadoFuncion(self, ctx:compiladoresParser.PrototipadoFuncionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#prototipadoFuncion.
    def exitPrototipadoFuncion(self, ctx:compiladoresParser.PrototipadoFuncionContext):
        pass


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


    # Enter a parse tree produced by compiladoresParser#operacion.
    def enterOperacion(self, ctx:compiladoresParser.OperacionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#operacion.
    def exitOperacion(self, ctx:compiladoresParser.OperacionContext):
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
                print("Error, la variable \""+str(nombre)+"\" no existe")
            if(str(caso) == 'creoInicializo'):
                self.tabla.addId(str(nombre),variable)
            if(str(caso) == 'creo'):
                self.tabla.addId(str(nombre),variable)
        else:
            if(str(caso) == 'uso'):
             resultado['usada'] = True
             self.tabla.addIdi(str(nombre),resultado,i)
            else:
             print("Error, la variable "+str(nombre)+" ya se encuentra creada")

del compiladoresParser