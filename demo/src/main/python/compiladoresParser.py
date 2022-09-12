# Generated from /home/pablo/Escritorio/Repositorios/DHS-Cursado/demo/src/main/python/compiladores.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3&")
        buf.write("-\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\30\n\3\3\4\3\4\5")
        buf.write("\4\34\n\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\2\2\t\2\4\6\b\n\f\16\2\2\2\'\2\20")
        buf.write("\3\2\2\2\4\27\3\2\2\2\6\33\3\2\2\2\b\35\3\2\2\2\n!\3\2")
        buf.write("\2\2\f%\3\2\2\2\16*\3\2\2\2\20\21\5\4\3\2\21\22\7\2\2")
        buf.write("\3\22\3\3\2\2\2\23\24\5\6\4\2\24\25\5\4\3\2\25\30\3\2")
        buf.write("\2\2\26\30\3\2\2\2\27\23\3\2\2\2\27\26\3\2\2\2\30\5\3")
        buf.write("\2\2\2\31\34\5\b\5\2\32\34\5\n\6\2\33\31\3\2\2\2\33\32")
        buf.write("\3\2\2\2\34\7\3\2\2\2\35\36\7\7\2\2\36\37\5\4\3\2\37 ")
        buf.write("\7\b\2\2 \t\3\2\2\2!\"\5\16\b\2\"#\7&\2\2#$\7\3\2\2$\13")
        buf.write("\3\2\2\2%&\7\f\2\2&\'\7\27\2\2\'(\7\13\2\2()\5\6\4\2)")
        buf.write("\r\3\2\2\2*+\7\26\2\2+\17\3\2\2\2\4\27\33")
        return buf.getvalue()


class compiladoresParser ( Parser ):

    grammarFileName = "compiladores.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "'.'", "' '", "'{'", "'}'", 
                     "'['", "']'", "')'", "'('", "'+'", "'-'", "'*'", "'/'", 
                     "'='", "'<'", "'>'", "'=='", "'!='", "'int'", "'if'", 
                     "'for'", "'while'", "'do'" ]

    symbolicNames = [ "<INVALID>", "PUNTOYCOMA", "COMA", "PUNTO", "ESPACIO", 
                      "LLAVEABRE", "LLAVECIERRA", "CORCHETEABRE", "CORCHETECIERRA", 
                      "PARENTESISCIERRA", "PARENTESISABRE", "MAS", "MENOS", 
                      "PRODUCTO", "DIVISION", "IGUAL", "MENOR", "MAYOR", 
                      "IGUALDAD", "NEGACION", "INT", "IF", "FOR", "WHILE", 
                      "DO", "FLOTANTES", "FLOTANTESNEGATIVOS", "HEXADECIMALES", 
                      "NUMERO", "PALABRA", "BYTE", "IP", "CORREO", "DOMINIO", 
                      "WS", "OTRO", "ID" ]

    RULE_prog = 0
    RULE_instrucciones = 1
    RULE_instruccion = 2
    RULE_bloque = 3
    RULE_declaracion = 4
    RULE_bloquewhile = 5
    RULE_tdato = 6

    ruleNames =  [ "prog", "instrucciones", "instruccion", "bloque", "declaracion", 
                   "bloquewhile", "tdato" ]

    EOF = Token.EOF
    PUNTOYCOMA=1
    COMA=2
    PUNTO=3
    ESPACIO=4
    LLAVEABRE=5
    LLAVECIERRA=6
    CORCHETEABRE=7
    CORCHETECIERRA=8
    PARENTESISCIERRA=9
    PARENTESISABRE=10
    MAS=11
    MENOS=12
    PRODUCTO=13
    DIVISION=14
    IGUAL=15
    MENOR=16
    MAYOR=17
    IGUALDAD=18
    NEGACION=19
    INT=20
    IF=21
    FOR=22
    WHILE=23
    DO=24
    FLOTANTES=25
    FLOTANTESNEGATIVOS=26
    HEXADECIMALES=27
    NUMERO=28
    PALABRA=29
    BYTE=30
    IP=31
    CORREO=32
    DOMINIO=33
    WS=34
    OTRO=35
    ID=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instrucciones(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionesContext,0)


        def EOF(self):
            return self.getToken(compiladoresParser.EOF, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = compiladoresParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.instrucciones()
            self.state = 15
            self.match(compiladoresParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def instrucciones(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionesContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_instrucciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrucciones" ):
                listener.enterInstrucciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrucciones" ):
                listener.exitInstrucciones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrucciones" ):
                return visitor.visitInstrucciones(self)
            else:
                return visitor.visitChildren(self)




    def instrucciones(self):

        localctx = compiladoresParser.InstruccionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instrucciones)
        try:
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [compiladoresParser.LLAVEABRE, compiladoresParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.instruccion()
                self.state = 18
                self.instrucciones()
                pass
            elif token in [compiladoresParser.EOF, compiladoresParser.LLAVECIERRA]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


        def declaracion(self):
            return self.getTypedRuleContext(compiladoresParser.DeclaracionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccion" ):
                return visitor.visitInstruccion(self)
            else:
                return visitor.visitChildren(self)




    def instruccion(self):

        localctx = compiladoresParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instruccion)
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [compiladoresParser.LLAVEABRE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.bloque()
                pass
            elif token in [compiladoresParser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.declaracion()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLAVEABRE(self):
            return self.getToken(compiladoresParser.LLAVEABRE, 0)

        def instrucciones(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionesContext,0)


        def LLAVECIERRA(self):
            return self.getToken(compiladoresParser.LLAVECIERRA, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = compiladoresParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(compiladoresParser.LLAVEABRE)
            self.state = 28
            self.instrucciones()
            self.state = 29
            self.match(compiladoresParser.LLAVECIERRA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tdato(self):
            return self.getTypedRuleContext(compiladoresParser.TdatoContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def PUNTOYCOMA(self):
            return self.getToken(compiladoresParser.PUNTOYCOMA, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion(self):

        localctx = compiladoresParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.tdato()
            self.state = 32
            self.match(compiladoresParser.ID)
            self.state = 33
            self.match(compiladoresParser.PUNTOYCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloquewhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARENTESISABRE(self):
            return self.getToken(compiladoresParser.PARENTESISABRE, 0)

        def IF(self):
            return self.getToken(compiladoresParser.IF, 0)

        def PARENTESISCIERRA(self):
            return self.getToken(compiladoresParser.PARENTESISCIERRA, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_bloquewhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloquewhile" ):
                listener.enterBloquewhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloquewhile" ):
                listener.exitBloquewhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloquewhile" ):
                return visitor.visitBloquewhile(self)
            else:
                return visitor.visitChildren(self)




    def bloquewhile(self):

        localctx = compiladoresParser.BloquewhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_bloquewhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(compiladoresParser.PARENTESISABRE)
            self.state = 36
            self.match(compiladoresParser.IF)
            self.state = 37
            self.match(compiladoresParser.PARENTESISCIERRA)
            self.state = 38
            self.instruccion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TdatoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(compiladoresParser.INT, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_tdato

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTdato" ):
                listener.enterTdato(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTdato" ):
                listener.exitTdato(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTdato" ):
                return visitor.visitTdato(self)
            else:
                return visitor.visitChildren(self)




    def tdato(self):

        localctx = compiladoresParser.TdatoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tdato)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(compiladoresParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





