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
            print(datos)
    #        self.f.write("\n")
    #        self.f.write(str(datos) + "--> exitItop")
    #        self.f.write("\n")
    #        self.f.write("\n")

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


    # Enter a parse tree produced by compiladoresParser#parentesis.
    def enterParentesis(self, ctx:compiladoresParser.ParentesisContext):
        pass

    # Exit a parse tree produced by compiladoresParser#parentesis.
    def exitParentesis(self, ctx:compiladoresParser.ParentesisContext):
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


    # Enter a parse tree produced by compiladoresParser#variable.
    def enterVariable(self, ctx:compiladoresParser.VariableContext):
        pass

    # Exit a parse tree produced by compiladoresParser#variable.
    def exitVariable(self, ctx:compiladoresParser.VariableContext):
        datos = ctx.getText()
        if(datos != ""):
            print(datos)
    #        self.f.write("\n")
    #        self.f.write(str(datos) + "--> exitVariable")
    #        self.f.write("\n")
    #        self.f.write("\n")

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
            print(datos)
    #        self.f.write("\n")
    #        self.f.write(str(datos) + "--> exitTdato")
    #        self.f.write("\n")
    #        self.f.write("\n")
            self.tipoDato = datos



     # Enter a parse tree produced by compiladoresParser#numero.
    def enterNumero(self, ctx:compiladoresParser.NumeroContext):
        pass

    # Exit a parse tree produced by compiladoresParser#numero.
    def exitNumero(self, ctx:compiladoresParser.NumeroContext):
        datos = ctx.getText()
        if(datos != ""):
            print(datos)
    #        self.f.write("\n")
    #        self.f.write(str(datos) + "--> exitNumero")
    #        self.f.write("\n")
    #        self.f.write("\n")

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
            print(datos)
    #        self.f.write("\n")
    #        self.f.write(str(datos) + "--> enterAsignacion")
    #        self.f.write("\n")
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
            print(datos)
    #        self.f.write("\n")
    #        self.f.write(str(datos) + "--> exitPrototipadoFuncion")
    #        self.f.write("\n")
    #        self.f.write("\n")
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
            print(datos)
    #        self.f.write("\n")
    #        self.f.write(str(datos) + "--> exitLlamadoAFunciones")
    #        self.f.write("\n")
    #        self.f.write("\n")
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


    # Enter a parse tree produced by compiladoresParser#bloqueElse.
    def enterBloqueElse(self, ctx:compiladoresParser.BloqueElseContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloqueElse.
    def exitBloqueElse(self, ctx:compiladoresParser.BloqueElseContext):
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

del compiladoresParser