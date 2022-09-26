from itertools import count
from antlr4 import *

from clases import Tabla, Variable
if __name__ is not None and "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser


# This class defines a complete listener for a parse tree produced by compiladoresParser.
class MiListener(ParseTreeListener):
    ts = Tabla()
    # Enter a parse tree produced by compiladoresParser#term.
    def exitTerm(self, ctx:compiladoresParser.TermContext):
        print ("Term tiene " + str(ctx.getChildCount()) + " hijos")
        print ("Term -> text |" + ctx.getText() + "|")


    # Enter a parse tree produced by compiladoresParser#factor.
    def enterFactor(self, ctx:compiladoresParser.FactorContext):
        print ("Factor IN -> |" + ctx.getText() + "|")
   #     self.ts.addContexto()
        

    # Exit a parse tree produced by compiladoresParser#factor.
    def exitFactor(self, ctx:compiladoresParser.FactorContext):
        print ("Factor OUT -> |" + ctx.getText() + "|")
   #     print ("Las variables -> |" + ctx.getChild())
   #     if(	ctx.getChildCount() > 0):
   #         self.ts.addId("VARIABLE",ctx.getChild())