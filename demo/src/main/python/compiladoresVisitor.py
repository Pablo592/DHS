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


    # Visit a parse tree produced by compiladoresParser#sumoResto.
    def visitSumoResto(self, ctx:compiladoresParser.SumoRestoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#pu.
    def visitPu(self, ctx:compiladoresParser.PuContext):
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



del compiladoresParser