
from antlr4 import *
from compiladoresVisitor import *
from compiladoresParser import *

class Caminante(compiladoresVisitor):
    contexto = 0
    
    f = open("output/Codigo_Intermedio.txt", "w")
    numeroVariable = 0
    ultimaVariable = ""
    parentesis = False
    instruccionParte = ""
    signo = ""
    instruccionLarga = ""
    primerInstruccion = ""


    # Visit a parse tree produced by compiladoresParser#itop.
    def visitItop(self, ctx:compiladoresParser.ItopContext):
        r = super().visitChildren(ctx)
 #       print("")
 #       print("")
 #       print("")
 #       print("+-+-+-+-+-+ visitItop +-+-+-+-+-+")
 #       for i in range(0,ctx.getChildCount()):
 #           print("+-+-+-+-+-+ OTRO HIJO +-+-+-+-+-+")
 #           print(ctx.getChild(i).getText())
 #           print("+-+-+-+-+-+-+-+ "+str(i)+" +-+-+-+-+-+-+-+-+")
        return r


    # Visit a parse tree produced by compiladoresParser#oparit.
    def visitOparit(self, ctx:compiladoresParser.OparitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#expo.
    def visitExpo(self, ctx:compiladoresParser.ExpoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#coma.
    def visitComa(self, ctx:compiladoresParser.ComaContext):
        return self.visitChildren(ctx)

    def visitTermino(self, ctx:compiladoresParser.TerminoContext):
        r = super().visitChildren(ctx)
        
        return r
    # Visit a parse tree produced by compiladoresParser#tie.
    def visitTie(self, ctx:compiladoresParser.TieContext):
        r = super().visitChildren(ctx)
        if(ctx.getChildCount() > 0):
            print("")
            print("")
            print("")
            print("+-+-+-+-+-+ visitTie +-+-+-+-+-+")
            for i in range(0,ctx.getChildCount()):
                print("+-+-+-+-+-+ OTRO HIJO +-+-+-+-+-+")
                print(ctx.getChild(i).getText())
                print("+-+-+-+-+-+-+-+ "+str(i)+" +-+-+-+-+-+-+-+-+")

            self.ultimaVariable = "t"+str(self.numeroVariable - 1)
            

            if(self.instruccionLarga != 1):
              if(ctx.getChild(1).getText() != ""):
                self.ultimaVariable =   ctx.getChild(1).getText().split("=")[1]

            else:
                if(self.instruccionParte in ctx.getChild(1).getText()):

                    aux = ctx.getChild(1).getText().split(self.instruccionParte)[0]
                    aux = aux.split("=")[1]
                    aux = aux[-1]
                    varAnterior = self.ultimaVariable
                    self.numeroVariable +=1
                    self.ultimaVariable = "t" + str(self.numeroVariable)
                    self.f.write(str(self.ultimaVariable) + " = " + str(aux)+ " "  + str(self.signo) + " " + str(varAnterior))
                    self.f.write("\n")

                
            if "*=" in ctx.getChild(1).getText():
                self.f.write(str(ctx.getChild(0).getText().split("*=")[0]) + " = " + str(ctx.getChild(0).getText().split("*=")[0]) + " * " + str(self.ultimaVariable))
                self.f.write("\n")

            elif "/=" in ctx.getChild(1).getText():
                self.f.write(str(ctx.getChild(0).getText().split("/=")[0]) + " = " + str(ctx.getChild(0).getText().split("/=")[0]) + " / " + str(self.ultimaVariable))
                self.f.write("\n")
            elif "%=" in ctx.getChild(1).getText():
                self.f.write(str(ctx.getChild(0).getText().split("%=")[0]) + " = " + str(ctx.getChild(0).getText().split("%=")[0]) + " % " + str(self.ultimaVariable))
                self.f.write("\n")
            elif "+=" in ctx.getChild(1).getText():
                self.f.write(str(ctx.getChild(0).getText().split("+=")[0]) + " = " + str(ctx.getChild(0).getText().split("+=")[0]) + " + " + str(self.ultimaVariable))
                self.f.write("\n")
            elif "-=" in ctx.getChild(1).getText():
                self.f.write(str(ctx.getChild(0).getText().split("-=")[0]) + " = " + str(ctx.getChild(0).getText().split("-=")[0]) + " - " + str(self.ultimaVariable))
                self.f.write("\n")
            elif "=" in ctx.getChild(1).getText():
                self.f.write(str(ctx.getChild(0).getText())+ " = " + self.ultimaVariable)
                self.f.write("\n")

            self.instruccionParte = ""
            self.numeroVariable = 0
            self.instruccionLarga = 0
            self.signo = ""

        return r


    # Visit a parse tree produced by compiladoresParser#igualOperaciones.
    def visitIgualOperaciones(self, ctx:compiladoresParser.IgualOperacionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#to.
    def visitTo(self, ctx:compiladoresParser.ToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#orLogico.
    def visitOrLogico(self, ctx:compiladoresParser.OrLogicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#ti.
    def visitTi(self, ctx:compiladoresParser.TiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#andLogico.
    def visitAndLogico(self, ctx:compiladoresParser.AndLogicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#te.
    def visitTe(self, ctx:compiladoresParser.TeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#igualo.
    def visitIgualo(self, ctx:compiladoresParser.IgualoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#po.
    def visitPo(self, ctx:compiladoresParser.PoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#relaciono.
    def visitRelaciono(self, ctx:compiladoresParser.RelacionoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#pi.
    def visitPi(self, ctx:compiladoresParser.PiContext):
        r = super().visitChildren(ctx)
        return r

    # Visit a parse tree produced by compiladoresParser#multiDivi.
    def visitMultiDivi(self, ctx:compiladoresParser.MultiDiviContext):
        r = super().visitChildren(ctx)
        return r

    # Visit a parse tree produced by compiladoresParser#parentesis.
    def visitParentesis(self, ctx:compiladoresParser.ParentesisContext):
        r = super().visitChildren(ctx)
        if(ctx.getChildCount() > 0):
            print("")
            print("")
            print("")
            print("+-+-+-+-+-+ visitParentesis +-+-+-+-+-+")
            for i in range(0,ctx.getChildCount()):
                print("+-+-+-+-+-+ OTRO HIJO +-+-+-+-+-+")
                print(ctx.getChild(i).getText())
                print("+-+-+-+-+-+-+-+ "+str(i)+" +-+-+-+-+-+-+-+-+")
        return r


    def visitT(self, ctx:compiladoresParser.TContext):
        r = super().visitChildren(ctx)
        if(ctx.getChildCount() > 0):
            print("")
            print("")
            print("")
            print("+-+-+-+-+-+ visitT +-+-+-+-+-+")
            for i in range(0,ctx.getChildCount()):
                print("+-+-+-+-+-+ OTRO HIJO +-+-+-+-+-+")
                print(ctx.getChild(i).getText())
                print("+-+-+-+-+-+-+-+ "+str(i)+" +-+-+-+-+-+-+-+-+")

            if(self.instruccionParte == ""):
                self.signo = ctx.getChild(0).getText()

                self.ultimaVariable = "t" + str(self.numeroVariable)

                self.primerInstruccion = str(self.ultimaVariable) + " = " + str(ctx.getChild(1).getText()) + "\n"
                self.instruccionParte =str(ctx.getChild(0).getText()) + str(ctx.getChild(1).getText())
                self.instruccionLarga = 0
                self.numeroVariable +=1
            else:
                if(str(ctx.getChild(0).getText()) != ""):
                    self.instruccionLarga = 1
                    if( str(self.ultimaVariable) == str("t" + str(self.numeroVariable - 1))):
                        self.instruccionParte = str(ctx.getChild(0).getText()) + str(ctx.getChild(1).getText()) + str(ctx.getChild(2).getText())

                        varAnterior = "t" + str(self.numeroVariable - 1)
                        self.ultimaVariable = "t" + str(self.numeroVariable)

                        self.f.write(self.primerInstruccion)
                        self.primerInstruccion = ""

                        if(("*" in str(ctx.getChild(1).getText())) | ("/" in str(ctx.getChild(1).getText()))):
             
                            self.f.write(str(self.ultimaVariable) + " = " + str(ctx.getChild(1).getText()))
                            self.f.write("\n")
                           
                            varAnteriorr = self.ultimaVariable
                            self.numeroVariable +=1
                            self.ultimaVariable = "t" + str(self.numeroVariable)   
                            self.f.write(str(self.ultimaVariable) + " = " + str(varAnteriorr)+ " "  + str(self.signo) + " " + str(varAnterior))
                            self.f.write("\n")
                            self.signo = ctx.getChild(0).getText()
                            self.numeroVariable +=1
                        else:
                            self.f.write(str(self.ultimaVariable) + " = " + str(ctx.getChild(1).getText())+ " "  + str(self.signo) + " " + str(varAnterior))
                            self.f.write("\n")
                            self.signo = ctx.getChild(0).getText()
                            self.numeroVariable +=1
    
            
        return r


    # Visit a parse tree produced by compiladoresParser#pe.
    def visitPe(self, ctx:compiladoresParser.PeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#prefijo.
    def visitPrefijo(self, ctx:compiladoresParser.PrefijoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#factor.
    def visitFactor(self, ctx:compiladoresParser.FactorContext):
        r = super().visitChildren(ctx)
        return r


    # Visit a parse tree produced by compiladoresParser#prog.
    def visitProg(self, ctx:compiladoresParser.ProgContext):
        print("\n")
        print("Comienza el recorrido del programa")
        r = super().visitChildren(ctx)
        print("Finaliza el recorrido del programa")
        return r


    # Visit a parse tree produced by compiladoresParser#instrucciones.
    def visitInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#instruccion.
    def visitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#variable.
    def visitVariable(self, ctx:compiladoresParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque.
    def visitBloque(self, ctx:compiladoresParser.BloqueContext):
        self.contexto += 1
  #      print("\t Entramos al contexto " + str(self.contexto))     
  #      print("\t\t Contenido |" + ctx.getText() + "|")
  #      print("\t\t Bloque tiene " + str(ctx.getChildCount()) + " hijos")     
  #      print("\t\t\t Hijo 0 " + ctx.getChild(0).getText() + " hijos")     
  #      print("\t\t\t Hijo 1 " + ctx.getChild(1).getText() + " hijos")     
  #      print("\t\t\t Hijo 2 " + ctx.getChild(2).getText() + " hijos")     
        r =  super().visitBloque(ctx)
  #      print("\t Salimos del contexto " + str(self.contexto))     
        self.contexto -= 1
        return r


    # Visit a parse tree produced by compiladoresParser#declaroAsigno.
    def visitDeclaroAsigno(self, ctx:compiladoresParser.DeclaroAsignoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#asignacion.
    def visitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#prototipadoFuncion.
    def visitPrototipadoFuncion(self, ctx:compiladoresParser.PrototipadoFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#llamadoAFunciones.
    def visitLlamadoAFunciones(self, ctx:compiladoresParser.LlamadoAFuncionesContext):
        r = super().visitChildren(ctx)
        if(ctx.getChildCount() > 0):
            print("")
            print("")
            print("")
            print("+-+-+-+-+-+ visitLlamadoAFunciones +-+-+-+-+-+")
            for i in range(0,ctx.getChildCount()):
                print("+-+-+-+-+-+ OTRO HIJO +-+-+-+-+-+")
                print(ctx.getChild(i).getText())
                print("+-+-+-+-+-+-+-+ "+str(i)+" +-+-+-+-+-+-+-+-+")
        return r


    # Visit a parse tree produced by compiladoresParser#desarrolloFuncion.
    def visitDesarrolloFuncion(self, ctx:compiladoresParser.DesarrolloFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#retorno.
    def visitRetorno(self, ctx:compiladoresParser.RetornoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloqueif.
    def visitBloqueif(self, ctx:compiladoresParser.BloqueifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloquewhile.
    def visitBloquewhile(self, ctx:compiladoresParser.BloquewhileContext):
        print("")
        print("")
        print("")
   #     print("+-+-+-+-+-+ WHILE +-+-+-+-+-+")
   #     for i in range(0,ctx.getChildCount()):
   #         print("+-+-+-+-+-+ OTRO HIJO +-+-+-+-+-+")
   #         print(ctx.getChild(i).getText())
   #         print("+-+-+-+-+-+-+-+ "+str(i)+" +-+-+-+-+-+-+-+-+")
        
        return super().visitChildren(ctx)



    # Visit a parse tree produced by compiladoresParser#bloquefor.
    def visitBloquefor(self, ctx:compiladoresParser.BloqueforContext):
  #      print("")
  #      print("")
  #      print("")
  #      print("+-+-+-+-+-+ FOR +-+-+-+-+-+")
  #      for i in range(0,ctx.getChildCount()):
  #          print("+-+-+-+-+-+ OTRO HIJO +-+-+-+-+-+")
  #          print(ctx.getChild(i).getText())
  #          print("+-+-+-+-+-+-+-+ "+str(i)+" +-+-+-+-+-+-+-+-+")
        return  super().visitBloque(ctx)

del compiladoresParser
