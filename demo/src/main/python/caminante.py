
from antlr4 import *
from compiladoresVisitor import *
from compiladoresParser import *

class Caminante(compiladoresVisitor):
    contexto = 0
    
    f = open("output/Codigo_Intermedio.txt", "w")

    # Visit a parse tree produced by compiladoresParser#itop.
    def visitItop(self, ctx:compiladoresParser.ItopContext):
        pass


    # Visit a parse tree produced by compiladoresParser#oparit.
    def visitOparit(self, ctx:compiladoresParser.OparitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#expo.
    def visitExpo(self, ctx:compiladoresParser.ExpoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#coma.
    def visitComa(self, ctx:compiladoresParser.ComaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#tie.
    def visitTie(self, ctx:compiladoresParser.TieContext):
        return self.visitChildren(ctx)


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
        return self.visitChildren(ctx)

    # Visit a parse tree produced by compiladoresParser#multiDivi.
    def visitMultiDivi(self, ctx:compiladoresParser.MultiDiviContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#pe.
    def visitPe(self, ctx:compiladoresParser.PeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#prefijo.
    def visitPrefijo(self, ctx:compiladoresParser.PrefijoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#factor.
    def visitFactor(self, ctx:compiladoresParser.FactorContext):
        return self.visitChildren(ctx)


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
        return self.visitChildren(ctx)


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
        numeroRegistro = 0
        numeroLabel = 0


        print("")
        print("")
        print("")
        print("+-+-+-+-+-+ WHILE +-+-+-+-+-+")
        for i in range(0,ctx.getChildCount()):
            print("+-+-+-+-+-+ OTRO HIJO +-+-+-+-+-+")
            print(ctx.getChild(i).getText())
            print("+-+-+-+-+-+-+-+ "+str(i)+" +-+-+-+-+-+-+-+-+")
        
        label = "l" + str(numeroLabel)
        puntoIni =  label
        self.f.write("label " + puntoIni + "\n")
        numeroLabel+=1
        label = "l" + str(numeroLabel)
        registro = "t"+ str(numeroRegistro)
        condicion = ctx.getChild(2).getText()
        self.f.write(registro + " = " + str(condicion) + "\n")
        self.f.write("ifnot " + registro + " jump " + label + "\n")
        cuerpo = ctx.getChild(4).getText()
        if "{" in cuerpo:
            cuerpo = cuerpo[1:-1]
        posiblesVariables = []
        for i in cuerpo.split(";"):
            numeroRegistro +=1
            registro = "t"+ str(numeroRegistro)

            if "*=" in i:
                partes = i.split("*=")
                if "+" in partes[1]:
                    if len(partes[1].split("+")) > 2:
                        op = partes[1]
                        operadores = []
                        aux1 = op.split('+')
                        for i in aux1:
                            if len(aux1) > 1:
                                operadores.append("+")
                            aux2 = i.split('-')
                            for j in aux2:
                                if len(aux2) > 1:
                                    operadores.append("-")
                                aux3 = j.split('*')
                                for k in aux3:
                                    if len(aux3) > 1:
                                        operadores.append("*")
                                    aux4 = k.split('/')
                                    for m in aux4:
                                        if len(aux4) > 1:
                                            operadores.append("/")
                                        posiblesVariables.append(m)

                        operadores.append("#")
                        contador = 0
                        filtrado = []
                        for p in range(0,len(operadores)-1):
                            
                            if(operadores[p] == "+"):
                                filtrado.append("+")

                            if(operadores[p] != "+"):
                                if(operadores[p] == operadores[p+1]):
                                    contador+=1
                                else:
                                    for i in range(0,contador):
                                        filtrado.append(operadores[p])
                                    contador = 0

                        print(str(posiblesVariables))
                        print(str(filtrado))

                    else:
                        self.f.write(registro + " = " + partes[1]  + "\n")
                        self.f.write(partes[0] + " = " + partes[0] + " * " + registro  + "\n")
                    
                       
            elif "/=" in i:
                partes = i.split("/=")
                self.f.write(registro + " = " + partes[1]  + "\n")
                self.f.write(partes[0] + " = " + partes[0] + " / " + registro  + "\n")
            elif "%=" in i:
                partes = i.split("%=")
                self.f.write(registro + " = " + partes[1]  + "\n")
                self.f.write(partes[0] + " = " + partes[0] + " % " + registro  + "\n")
            elif "+=" in i:
                partes = i.split("+=")
                self.f.write(registro + " = " + partes[1]  + "\n")
                self.f.write(partes[0] + " = " + partes[0] + " + " + registro  + "\n")
            elif "-=" in i:
                partes = i.split("-=")
                self.f.write(registro + " = " + partes[1]  + "\n")
                self.f.write(partes[0] + " = " + partes[0] + " - " + registro  + "\n")
            elif "=" in i:
                self.f.write(i + "\n")

        label = "l" + str(numeroLabel)
        self.f.write("jump " + puntoIni + "\n")
        self.f.write(label + "\n")


        return self.visitChildren(ctx)



    # Visit a parse tree produced by compiladoresParser#bloquefor.
    def visitBloquefor(self, ctx:compiladoresParser.BloqueforContext):
        print("")
        print("")
        print("")
        print("+-+-+-+-+-+ FOR +-+-+-+-+-+")
        for i in range(0,ctx.getChildCount()):
            print("+-+-+-+-+-+ OTRO HIJO +-+-+-+-+-+")
            print(ctx.getChild(i).getText())
            print("+-+-+-+-+-+-+-+ "+str(i)+" +-+-+-+-+-+-+-+-+")
        return self.visitChildren(ctx)




del compiladoresParser
