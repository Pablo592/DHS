# Generated from /home/pablo/Escritorio/Repositorios/DHS-Cursado/demo/src/main/python/compiladores.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete generic visitor for a parse tree produced by compiladoresParser.

class compiladoresVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by compiladoresParser#si.
    def visitSi(self, ctx:compiladoresParser.SiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#s.
    def visitS(self, ctx:compiladoresParser.SContext):
        return self.visitChildren(ctx)



del compiladoresParser