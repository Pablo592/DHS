# Generated from /home/pablo/Escritorio/Repositorios/DHS-Cursado/demo/src/main/python/compiladores.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete generic visitor for a parse tree produced by compiladoresParser.

class compiladoresVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by compiladoresParser#itop.
    def visitItop(self, ctx:compiladoresParser.ItopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#oparit.
    def visitOparit(self, ctx:compiladoresParser.OparitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#exp.
    def visitExp(self, ctx:compiladoresParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#to.
    def visitTo(self, ctx:compiladoresParser.ToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#op.
    def visitOp(self, ctx:compiladoresParser.OpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#term.
    def visitTerm(self, ctx:compiladoresParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#t.
    def visitT(self, ctx:compiladoresParser.TContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#factor.
    def visitFactor(self, ctx:compiladoresParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#f.
    def visitF(self, ctx:compiladoresParser.FContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#prog.
    def visitProg(self, ctx:compiladoresParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#instrucciones.
    def visitInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#instruccion.
    def visitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque.
    def visitBloque(self, ctx:compiladoresParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#declaracion.
    def visitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloquefor.
    def visitBloquefor(self, ctx:compiladoresParser.BloqueforContext):
        return self.visitChildren(ctx)



del compiladoresParser