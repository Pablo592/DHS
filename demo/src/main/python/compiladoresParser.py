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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3%")
        buf.write("\34\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\32\n\3")
        buf.write("\3\3\2\2\4\2\4\2\2\2\34\2\6\3\2\2\2\4\31\3\2\2\2\6\7\5")
        buf.write("\4\3\2\7\b\7\2\2\3\b\3\3\2\2\2\t\n\7\f\2\2\n\13\5\4\3")
        buf.write("\2\13\f\7\13\2\2\f\r\5\4\3\2\r\32\3\2\2\2\16\17\7\t\2")
        buf.write("\2\17\20\5\4\3\2\20\21\7\n\2\2\21\22\5\4\3\2\22\32\3\2")
        buf.write("\2\2\23\24\7\7\2\2\24\25\5\4\3\2\25\26\7\b\2\2\26\27\5")
        buf.write("\4\3\2\27\32\3\2\2\2\30\32\3\2\2\2\31\t\3\2\2\2\31\16")
        buf.write("\3\2\2\2\31\23\3\2\2\2\31\30\3\2\2\2\32\5\3\2\2\2\3\31")
        return buf.getvalue()


class compiladoresParser ( Parser ):

    grammarFileName = "compiladores.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "'.'", "' '", "'{'", "'}'", 
                     "'['", "']'", "')'", "'('", "'+'", "'-'", "'*'", "'/'", 
                     "'='", "'<'", "'>'", "'=='", "'!='", "'if'", "'for'", 
                     "'while'", "'do'" ]

    symbolicNames = [ "<INVALID>", "PUNTOYCOMA", "COMA", "PUNTO", "ESPACIO", 
                      "LLAVEABRE", "LLAVECIERRA", "CORCHETEABRE", "CORCHETECIERRA", 
                      "PARENTESISCIERRA", "PARENTESISABRE", "MAS", "MENOS", 
                      "PRODUCTO", "DIVISION", "IGUAL", "MENOR", "MAYOR", 
                      "IGUALDAD", "NEGACION", "IF", "FOR", "WHILE", "DO", 
                      "FLOTANTES", "FLOTANTESNEGATIVOS", "HEXADECIMALES", 
                      "NUMERO", "PALABRA", "BYTE", "IP", "CORREO", "DOMINIO", 
                      "WS", "OTRO", "ID" ]

    RULE_si = 0
    RULE_s = 1

    ruleNames =  [ "si", "s" ]

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
    IF=20
    FOR=21
    WHILE=22
    DO=23
    FLOTANTES=24
    FLOTANTESNEGATIVOS=25
    HEXADECIMALES=26
    NUMERO=27
    PALABRA=28
    BYTE=29
    IP=30
    CORREO=31
    DOMINIO=32
    WS=33
    OTRO=34
    ID=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s(self):
            return self.getTypedRuleContext(compiladoresParser.SContext,0)


        def EOF(self):
            return self.getToken(compiladoresParser.EOF, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_si

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSi" ):
                listener.enterSi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSi" ):
                listener.exitSi(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSi" ):
                return visitor.visitSi(self)
            else:
                return visitor.visitChildren(self)




    def si(self):

        localctx = compiladoresParser.SiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_si)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.s()
            self.state = 5
            self.match(compiladoresParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARENTESISABRE(self):
            return self.getToken(compiladoresParser.PARENTESISABRE, 0)

        def s(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladoresParser.SContext)
            else:
                return self.getTypedRuleContext(compiladoresParser.SContext,i)


        def PARENTESISCIERRA(self):
            return self.getToken(compiladoresParser.PARENTESISCIERRA, 0)

        def CORCHETEABRE(self):
            return self.getToken(compiladoresParser.CORCHETEABRE, 0)

        def CORCHETECIERRA(self):
            return self.getToken(compiladoresParser.CORCHETECIERRA, 0)

        def LLAVEABRE(self):
            return self.getToken(compiladoresParser.LLAVEABRE, 0)

        def LLAVECIERRA(self):
            return self.getToken(compiladoresParser.LLAVECIERRA, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitS" ):
                return visitor.visitS(self)
            else:
                return visitor.visitChildren(self)




    def s(self):

        localctx = compiladoresParser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_s)
        try:
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [compiladoresParser.PARENTESISABRE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 7
                self.match(compiladoresParser.PARENTESISABRE)
                self.state = 8
                self.s()
                self.state = 9
                self.match(compiladoresParser.PARENTESISCIERRA)
                self.state = 10
                self.s()
                pass
            elif token in [compiladoresParser.CORCHETEABRE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 12
                self.match(compiladoresParser.CORCHETEABRE)
                self.state = 13
                self.s()
                self.state = 14
                self.match(compiladoresParser.CORCHETECIERRA)
                self.state = 15
                self.s()
                pass
            elif token in [compiladoresParser.LLAVEABRE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 17
                self.match(compiladoresParser.LLAVEABRE)
                self.state = 18
                self.s()
                self.state = 19
                self.match(compiladoresParser.LLAVECIERRA)
                self.state = 20
                self.s()
                pass
            elif token in [compiladoresParser.EOF, compiladoresParser.LLAVECIERRA, compiladoresParser.CORCHETECIERRA, compiladoresParser.PARENTESISCIERRA]:
                self.enterOuterAlt(localctx, 4)

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





