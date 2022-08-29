# Generated from /home/pablo/Escritorio/DHS-Cursado/demo/src/main/python/compiladores.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\35")
        buf.write("Z\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\5\2X\n\2\3\2\2\2\3\2\2\2\2t\2W\3\2")
        buf.write("\2\2\4X\3\2\2\2\5\6\7\27\2\2\6\7\b\2\1\2\7X\5\2\2\2\b")
        buf.write("\t\7\3\2\2\t\n\b\2\1\2\nX\5\2\2\2\13\f\7\4\2\2\f\r\b\2")
        buf.write("\1\2\rX\5\2\2\2\16\17\7\5\2\2\17\20\b\2\1\2\20X\5\2\2")
        buf.write("\2\21\22\7\6\2\2\22\23\b\2\1\2\23X\5\2\2\2\24\25\7\7\2")
        buf.write("\2\25\26\b\2\1\2\26X\5\2\2\2\27\30\7\b\2\2\30\31\b\2\1")
        buf.write("\2\31X\5\2\2\2\32\33\7\t\2\2\33\34\b\2\1\2\34X\5\2\2\2")
        buf.write("\35\36\7\n\2\2\36\37\b\2\1\2\37X\5\2\2\2 !\7\13\2\2!\"")
        buf.write("\b\2\1\2\"X\5\2\2\2#$\7\f\2\2$%\b\2\1\2%X\5\2\2\2&\'\7")
        buf.write("\r\2\2\'(\b\2\1\2(X\5\2\2\2)*\7\16\2\2*+\b\2\1\2+X\5\2")
        buf.write("\2\2,-\7\17\2\2-.\b\2\1\2.X\5\2\2\2/\60\7\20\2\2\60\61")
        buf.write("\b\2\1\2\61X\5\2\2\2\62\63\7\21\2\2\63\64\b\2\1\2\64X")
        buf.write("\5\2\2\2\65\66\7\22\2\2\66\67\b\2\1\2\67X\5\2\2\289\7")
        buf.write("\23\2\29:\b\2\1\2:X\5\2\2\2;<\7\24\2\2<=\b\2\1\2=X\5\2")
        buf.write("\2\2>?\7\25\2\2?@\b\2\1\2@X\5\2\2\2AB\7\26\2\2BC\b\2\1")
        buf.write("\2CX\5\2\2\2DE\7\30\2\2EF\b\2\1\2FX\5\2\2\2GH\7\31\2\2")
        buf.write("HI\b\2\1\2IX\5\2\2\2JK\7\32\2\2KL\b\2\1\2LX\5\2\2\2MN")
        buf.write("\7\33\2\2NO\b\2\1\2OX\5\2\2\2PQ\7\35\2\2QR\b\2\1\2RX\5")
        buf.write("\2\2\2ST\7\34\2\2TU\b\2\1\2UX\5\2\2\2VX\7\2\2\3W\4\3\2")
        buf.write("\2\2W\5\3\2\2\2W\b\3\2\2\2W\13\3\2\2\2W\16\3\2\2\2W\21")
        buf.write("\3\2\2\2W\24\3\2\2\2W\27\3\2\2\2W\32\3\2\2\2W\35\3\2\2")
        buf.write("\2W \3\2\2\2W#\3\2\2\2W&\3\2\2\2W)\3\2\2\2W,\3\2\2\2W")
        buf.write("/\3\2\2\2W\62\3\2\2\2W\65\3\2\2\2W8\3\2\2\2W;\3\2\2\2")
        buf.write("W>\3\2\2\2WA\3\2\2\2WD\3\2\2\2WG\3\2\2\2WJ\3\2\2\2WM\3")
        buf.write("\2\2\2WP\3\2\2\2WS\3\2\2\2WV\3\2\2\2X\3\3\2\2\2\3W")
        return buf.getvalue()


class compiladoresParser ( Parser ):

    grammarFileName = "compiladores.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "'.'", "'{'", "'}'", "'['", 
                     "']'", "')'", "'('", "<INVALID>", "<INVALID>", "'=='", 
                     "'!='", "'if'", "'for'", "'while'", "'do'" ]

    symbolicNames = [ "<INVALID>", "PUNTOYCOMA", "COMA", "PUNTO", "LLAVEABRE", 
                      "LLAVECIERRA", "CORCHETEABRE", "CORCHETECIERRA", "PARENTESISCIERRA", 
                      "PARENTESISABRE", "OP", "OPREL", "IGUALDAD", "NEGACION", 
                      "IF", "FOR", "WHILE", "DO", "FLOTANTES", "FLOTANTESNEGATIVOS", 
                      "HEXADECIMALES", "NUMERO", "PALABRA", "IP", "DOMINIO", 
                      "CORREO", "OTRO", "ID" ]

    RULE_s = 0

    ruleNames =  [ "s" ]

    EOF = Token.EOF
    PUNTOYCOMA=1
    COMA=2
    PUNTO=3
    LLAVEABRE=4
    LLAVECIERRA=5
    CORCHETEABRE=6
    CORCHETECIERRA=7
    PARENTESISCIERRA=8
    PARENTESISABRE=9
    OP=10
    OPREL=11
    IGUALDAD=12
    NEGACION=13
    IF=14
    FOR=15
    WHILE=16
    DO=17
    FLOTANTES=18
    FLOTANTESNEGATIVOS=19
    HEXADECIMALES=20
    NUMERO=21
    PALABRA=22
    IP=23
    DOMINIO=24
    CORREO=25
    OTRO=26
    ID=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._NUMERO = None # Token
            self._PUNTOYCOMA = None # Token
            self._COMA = None # Token
            self._PUNTO = None # Token
            self._LLAVEABRE = None # Token
            self._LLAVECIERRA = None # Token
            self._CORCHETEABRE = None # Token
            self._CORCHETECIERRA = None # Token
            self._PARENTESISCIERRA = None # Token
            self._PARENTESISABRE = None # Token
            self._OP = None # Token
            self._OPREL = None # Token
            self._IGUALDAD = None # Token
            self._NEGACION = None # Token
            self._IF = None # Token
            self._FOR = None # Token
            self._WHILE = None # Token
            self._DO = None # Token
            self._FLOTANTES = None # Token
            self._FLOTANTESNEGATIVOS = None # Token
            self._HEXADECIMALES = None # Token
            self._PALABRA = None # Token
            self._IP = None # Token
            self._DOMINIO = None # Token
            self._CORREO = None # Token
            self._ID = None # Token
            self._OTRO = None # Token

        def NUMERO(self):
            return self.getToken(compiladoresParser.NUMERO, 0)

        def s(self):
            return self.getTypedRuleContext(compiladoresParser.SContext,0)


        def PUNTOYCOMA(self):
            return self.getToken(compiladoresParser.PUNTOYCOMA, 0)

        def COMA(self):
            return self.getToken(compiladoresParser.COMA, 0)

        def PUNTO(self):
            return self.getToken(compiladoresParser.PUNTO, 0)

        def LLAVEABRE(self):
            return self.getToken(compiladoresParser.LLAVEABRE, 0)

        def LLAVECIERRA(self):
            return self.getToken(compiladoresParser.LLAVECIERRA, 0)

        def CORCHETEABRE(self):
            return self.getToken(compiladoresParser.CORCHETEABRE, 0)

        def CORCHETECIERRA(self):
            return self.getToken(compiladoresParser.CORCHETECIERRA, 0)

        def PARENTESISCIERRA(self):
            return self.getToken(compiladoresParser.PARENTESISCIERRA, 0)

        def PARENTESISABRE(self):
            return self.getToken(compiladoresParser.PARENTESISABRE, 0)

        def OP(self):
            return self.getToken(compiladoresParser.OP, 0)

        def OPREL(self):
            return self.getToken(compiladoresParser.OPREL, 0)

        def IGUALDAD(self):
            return self.getToken(compiladoresParser.IGUALDAD, 0)

        def NEGACION(self):
            return self.getToken(compiladoresParser.NEGACION, 0)

        def IF(self):
            return self.getToken(compiladoresParser.IF, 0)

        def FOR(self):
            return self.getToken(compiladoresParser.FOR, 0)

        def WHILE(self):
            return self.getToken(compiladoresParser.WHILE, 0)

        def DO(self):
            return self.getToken(compiladoresParser.DO, 0)

        def FLOTANTES(self):
            return self.getToken(compiladoresParser.FLOTANTES, 0)

        def FLOTANTESNEGATIVOS(self):
            return self.getToken(compiladoresParser.FLOTANTESNEGATIVOS, 0)

        def HEXADECIMALES(self):
            return self.getToken(compiladoresParser.HEXADECIMALES, 0)

        def PALABRA(self):
            return self.getToken(compiladoresParser.PALABRA, 0)

        def IP(self):
            return self.getToken(compiladoresParser.IP, 0)

        def DOMINIO(self):
            return self.getToken(compiladoresParser.DOMINIO, 0)

        def CORREO(self):
            return self.getToken(compiladoresParser.CORREO, 0)

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def OTRO(self):
            return self.getToken(compiladoresParser.OTRO, 0)

        def EOF(self):
            return self.getToken(compiladoresParser.EOF, 0)

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
        self.enterRule(localctx, 0, self.RULE_s)
        try:
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 3
                localctx._NUMERO = self.match(compiladoresParser.NUMERO)
                print("NUMERO ->" + (None if localctx._NUMERO is None else localctx._NUMERO.text) + "<--") 
                self.state = 5
                self.s()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 6
                localctx._PUNTOYCOMA = self.match(compiladoresParser.PUNTOYCOMA)
                print("PUNTOYCOMA ->" + (None if localctx._PUNTOYCOMA is None else localctx._PUNTOYCOMA.text) + "<--") 
                self.state = 8
                self.s()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 9
                localctx._COMA = self.match(compiladoresParser.COMA)
                print("COMA ->" + (None if localctx._COMA is None else localctx._COMA.text) + "<--") 
                self.state = 11
                self.s()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 12
                localctx._PUNTO = self.match(compiladoresParser.PUNTO)
                print("PUNTO ->" + (None if localctx._PUNTO is None else localctx._PUNTO.text) + "<--") 
                self.state = 14
                self.s()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 15
                localctx._LLAVEABRE = self.match(compiladoresParser.LLAVEABRE)
                print("LLAVEABRE ->" + (None if localctx._LLAVEABRE is None else localctx._LLAVEABRE.text) + "<--") 
                self.state = 17
                self.s()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 18
                localctx._LLAVECIERRA = self.match(compiladoresParser.LLAVECIERRA)
                print("LLAVECIERRA ->" + (None if localctx._LLAVECIERRA is None else localctx._LLAVECIERRA.text) + "<--") 
                self.state = 20
                self.s()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 21
                localctx._CORCHETEABRE = self.match(compiladoresParser.CORCHETEABRE)
                print("CORCHETEABRE ->" + (None if localctx._CORCHETEABRE is None else localctx._CORCHETEABRE.text) + "<--") 
                self.state = 23
                self.s()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 24
                localctx._CORCHETECIERRA = self.match(compiladoresParser.CORCHETECIERRA)
                print("CORCHETECIERRA ->" + (None if localctx._CORCHETECIERRA is None else localctx._CORCHETECIERRA.text) + "<--") 
                self.state = 26
                self.s()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 27
                localctx._PARENTESISCIERRA = self.match(compiladoresParser.PARENTESISCIERRA)
                print("PARENTESISCIERRA ->" + (None if localctx._PARENTESISCIERRA is None else localctx._PARENTESISCIERRA.text) + "<--") 
                self.state = 29
                self.s()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 30
                localctx._PARENTESISABRE = self.match(compiladoresParser.PARENTESISABRE)
                print("PARENTESISABRE ->" + (None if localctx._PARENTESISABRE is None else localctx._PARENTESISABRE.text) + "<--") 
                self.state = 32
                self.s()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 33
                localctx._OP = self.match(compiladoresParser.OP)
                print("OP ->" + (None if localctx._OP is None else localctx._OP.text) + "<--") 
                self.state = 35
                self.s()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 36
                localctx._OPREL = self.match(compiladoresParser.OPREL)
                print("OPREL ->" + (None if localctx._OPREL is None else localctx._OPREL.text) + "<--") 
                self.state = 38
                self.s()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 39
                localctx._IGUALDAD = self.match(compiladoresParser.IGUALDAD)
                print("IGUALDAD ->" + (None if localctx._IGUALDAD is None else localctx._IGUALDAD.text) + "<--") 
                self.state = 41
                self.s()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 42
                localctx._NEGACION = self.match(compiladoresParser.NEGACION)
                print("NEGACION ->" + (None if localctx._NEGACION is None else localctx._NEGACION.text) + "<--") 
                self.state = 44
                self.s()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 45
                localctx._IF = self.match(compiladoresParser.IF)
                print("IF ->" + (None if localctx._IF is None else localctx._IF.text) + "<--") 
                self.state = 47
                self.s()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 48
                localctx._FOR = self.match(compiladoresParser.FOR)
                print("FOR ->" + (None if localctx._FOR is None else localctx._FOR.text) + "<--") 
                self.state = 50
                self.s()
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 51
                localctx._WHILE = self.match(compiladoresParser.WHILE)
                print("WHILE ->" + (None if localctx._WHILE is None else localctx._WHILE.text) + "<--") 
                self.state = 53
                self.s()
                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
                self.state = 54
                localctx._DO = self.match(compiladoresParser.DO)
                print("DO ->" + (None if localctx._DO is None else localctx._DO.text) + "<--") 
                self.state = 56
                self.s()
                pass

            elif la_ == 20:
                self.enterOuterAlt(localctx, 20)
                self.state = 57
                localctx._FLOTANTES = self.match(compiladoresParser.FLOTANTES)
                print("FLOTANTES ->" + (None if localctx._FLOTANTES is None else localctx._FLOTANTES.text) + "<--") 
                self.state = 59
                self.s()
                pass

            elif la_ == 21:
                self.enterOuterAlt(localctx, 21)
                self.state = 60
                localctx._FLOTANTESNEGATIVOS = self.match(compiladoresParser.FLOTANTESNEGATIVOS)
                print("FLOTANTESNEGATIVOS ->" + (None if localctx._FLOTANTESNEGATIVOS is None else localctx._FLOTANTESNEGATIVOS.text) + "<--") 
                self.state = 62
                self.s()
                pass

            elif la_ == 22:
                self.enterOuterAlt(localctx, 22)
                self.state = 63
                localctx._HEXADECIMALES = self.match(compiladoresParser.HEXADECIMALES)
                print("HEXADECIMALES ->" + (None if localctx._HEXADECIMALES is None else localctx._HEXADECIMALES.text) + "<--") 
                self.state = 65
                self.s()
                pass

            elif la_ == 23:
                self.enterOuterAlt(localctx, 23)
                self.state = 66
                localctx._PALABRA = self.match(compiladoresParser.PALABRA)
                print("PALABRA ->" + (None if localctx._PALABRA is None else localctx._PALABRA.text) + "<--") 
                self.state = 68
                self.s()
                pass

            elif la_ == 24:
                self.enterOuterAlt(localctx, 24)
                self.state = 69
                localctx._IP = self.match(compiladoresParser.IP)
                print("IP ->" + (None if localctx._IP is None else localctx._IP.text) + "<--") 
                self.state = 71
                self.s()
                pass

            elif la_ == 25:
                self.enterOuterAlt(localctx, 25)
                self.state = 72
                localctx._DOMINIO = self.match(compiladoresParser.DOMINIO)
                print("DOMINIO ->" + (None if localctx._DOMINIO is None else localctx._DOMINIO.text) + "<--") 
                self.state = 74
                self.s()
                pass

            elif la_ == 26:
                self.enterOuterAlt(localctx, 26)
                self.state = 75
                localctx._CORREO = self.match(compiladoresParser.CORREO)
                print("CORREO ->" + (None if localctx._CORREO is None else localctx._CORREO.text) + "<--") 
                self.state = 77
                self.s()
                pass

            elif la_ == 27:
                self.enterOuterAlt(localctx, 27)
                self.state = 78
                localctx._ID = self.match(compiladoresParser.ID)
                print("ID ->" + (None if localctx._ID is None else localctx._ID.text) + "<--") 
                self.state = 80
                self.s()
                pass

            elif la_ == 28:
                self.enterOuterAlt(localctx, 28)
                self.state = 81
                localctx._OTRO = self.match(compiladoresParser.OTRO)
                print("Otro ->" + (None if localctx._OTRO is None else localctx._OTRO.text) + "<--") 
                self.state = 83
                self.s()
                pass

            elif la_ == 29:
                self.enterOuterAlt(localctx, 29)
                self.state = 84
                self.match(compiladoresParser.EOF)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





