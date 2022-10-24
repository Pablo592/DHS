grammar compiladores;

fragment LETRA: [A-Za-z];
fragment DIGITO: [0-9];
PUNTOYCOMA: ';';
COMA: ',';
PUNTO: '.';
LLAVEABRE: '{';
LLAVECIERRA: '}';
CORCHETEABRE: '[';
CORCHETECIERRA: ']';
PARENTESISCIERRA: ')';
PARENTESISABRE: '(';
OP: MAS|MENOS|PRODUCTO|DIVISION;
MAS: '+';
MENOS: '-';
PRODUCTO: '*';
DIVISION: '/';
RESTO:'%';
CONDICIONAL: MENOR | MAYOR | IGUALDAD | DISTINTO;
OPIGUAL: IGUAL | PRODUCTOIGUAL | DIVIDIDOIGUAL | RESTOIGUAL | MASIGUAL | MENOSIGUAL;
IGUAL: '=';
PRODUCTOIGUAL:'*=';
IGUALDAD: '==';
DIVIDIDOIGUAL:'/=';
RESTOIGUAL:'%=';
MASIGUAL:'+=';
MENOSIGUAL:'-=';
MAYORIGUAL:'>=';
MENORIGUAL:'<=';
MENOR: '<';
MAYOR: '>';
AND : '&&';
OR : '||';
DISTINTO: '!=';
NEGACION: '!';
SUMAUNO: '++';
RESTAUNO: '--';
BOOLEANOS: 'true' | 'false';
TDATO :INT
      |STRING
      |FLOAT
      |DOUBLE
      |LONG
      ;
INT: 'int';
STRING: 'string';
FLOAT: 'float';
DOUBLE: 'double';
LONG: 'long';
IF: 'if';
ELSE: 'else';
FOR: 'for';
WHILE: 'while';
DO: 'do';
FLOTANTES: DIGITO PUNTO DIGITO;
FLOTANTESNEGATIVOS: '-' DIGITO PUNTO DIGITO;
NUMERO: ('-' (DIGITO+)) | (DIGITO+);

VARIABLE: (LETRA | '_') (LETRA | DIGITO | '_')*;

WS: [ \t\n\r] -> skip;
COMENTARIOS: ('/*'.'*/') '//' -> skip;
OTRO: .;

 //Verifico que todos los parentesis se abran y se cierren fragment //Analisis sintactico
// descendente ----> Voy de la raiz a las hojas // antlr4 usa descendente
 
// Raiz//d si : s EOF;
 
 //s : PARENTESISABRE s PARENTESISCIERRA s // | CORCHETEABRE s CORCHETECIERRA s // | LLAVEABRE s
// LLAVECIERRA s // | // ;


itop : oparit itop
     |
     ;

oparit : expo
       ;

expo : tie coma;

coma: COMA tie coma
    | PUNTOYCOMA tie coma
    |
    ;

tie : to igualOperaciones;

igualOperaciones:IGUAL to igualOperaciones
                |PRODUCTOIGUAL to igualOperaciones
                |DIVIDIDOIGUAL to igualOperaciones
                |RESTOIGUAL to igualOperaciones
                |MASIGUAL to igualOperaciones
                |MENOSIGUAL to igualOperaciones
                |
                ;
         

to: ti orLogico;

orLogico: OR ti orLogico
        |
        ;

ti: te andLogico;

andLogico: AND te andLogico
         |
         ;

te: po igualo;

igualo:IGUALDAD po igualo
      |DISTINTO po igualo
      |
      ;

po: pi relaciono;

relaciono:MAYOR pi relaciono
         |MENOR pi relaciono
         |MAYORIGUAL pi relaciono
         |MENORIGUAL pi relaciono
         |
         ;

pi: termino t;

t : MAS termino t
  | MENOS termino t
  |
  ;

termino: pe multiDivi;

multiDivi:PRODUCTO pe multiDivi
         |DIVISION pe multiDivi
         |RESTO pe multiDivi
         |
         ;

pe: factor prefijo;


prefijo:RESTAUNO VARIABLE factor prefijo
       |SUMAUNO VARIABLE factor prefijo
       |NEGACION factor prefijo
       |
       ;


factor : VARIABLE
       | NUMERO
       | PARENTESISABRE expo PARENTESISCIERRA
       ;
       
  
prog : instrucciones EOF ;
instrucciones : instruccion instrucciones
              |
              ;

instruccion : bloque
            | llamadoAFunciones PUNTOYCOMA
            | declaracion PUNTOYCOMA
            | declaroAsigno PUNTOYCOMA
            | operacion PUNTOYCOMA
            | asignacion PUNTOYCOMA
            | prototipadoFuncion PUNTOYCOMA
            | desarrolloFuncion
            | retorno PUNTOYCOMA
            | bloqueif
            | bloquefor
            | bloquewhile
            ;
variable:VARIABLE;
bloque : LLAVEABRE instrucciones LLAVECIERRA;
declaracion : TDATO (COMA|variable)+;
declaroAsigno : TDATO (COMA|(variable ((OPIGUAL (NUMERO|variable|llamadoAFunciones|operacion))| SUMAUNO)| variable|NUMERO))+;


asignacion :  (variable ((OPIGUAL (operacion|NUMERO|variable|llamadoAFunciones))| SUMAUNO))+;
prototipadoFuncion : TDATO variable PARENTESISABRE (TDATO (variable|NUMERO) (COMA|))* PARENTESISCIERRA;
llamadoAFunciones: variable PARENTESISABRE ((variable|NUMERO) (COMA|))* PARENTESISCIERRA;
desarrolloFuncion: TDATO variable PARENTESISABRE (TDATO (variable|NUMERO) (COMA|))* PARENTESISCIERRA instruccion;
operacion: ( (variable|NUMERO|) OP (variable|NUMERO))+;
retorno: 'return' (NUMERO|variable);
bloqueif: IF PARENTESISABRE (((NUMERO|variable)CONDICIONAL(NUMERO|variable))|BOOLEANOS) PARENTESISCIERRA instruccion ((ELSE instruccion)|);
bloquewhile: WHILE PARENTESISABRE (((NUMERO|variable)CONDICIONAL(NUMERO|variable))|BOOLEANOS) PARENTESISCIERRA instruccion;
bloquefor: FOR PARENTESISABRE (asignacion|declaracion) PUNTOYCOMA (((NUMERO|variable)CONDICIONAL(NUMERO|variable))*|BOOLEANOS) PUNTOYCOMA (asignacion|OP)* PARENTESISCIERRA bloque;
 
//bloquewhile: PARENTESISABRE IF PARENTESISCIERRA instruccion;

//Analisis sintactico Ascendente ----> Voy de las hojas a la raiz

//variable, asignar variables, llamado a funciones, prototipado, bucles, if

// bloquewhile : PA comparacion/opal PC instruccion ;


/*
variable:VARIABLE
        |NUMERO
        |VARIABLE RESTAUNO
        |VARIABLE SUMAUNO
        |
        ; */