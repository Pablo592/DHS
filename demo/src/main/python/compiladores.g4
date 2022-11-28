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
//OP: MAS|MENOS|PRODUCTO|DIVISION;
MAS: '+';
MENOS: '-';
PRODUCTO: '*';
DIVISION: '/';
RESTO:'%';
//CONDICIONAL: MENOR | MAYOR | IGUALDAD | DISTINTO;
//OPIGUAL: IGUAL | PRODUCTOIGUAL | DIVIDIDOIGUAL | RESTOIGUAL | MASIGUAL | MENOSIGUAL;
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

pe: factor | prefijo;


prefijo:RESTAUNO variable factor prefijo
       |SUMAUNO variable factor prefijo
       |NEGACION factor prefijo
       ;


factor : llamadoAFunciones 
       | variable
       | numero
       | FLOTANTES
       | FLOTANTESNEGATIVOS
       | parentesis
       | variable SUMAUNO
       | variable RESTAUNO
       ;

parentesis: PARENTESISABRE expo PARENTESISCIERRA
          ;

  
prog : instrucciones EOF ;
instrucciones : instruccion instrucciones
              |
              ;

instruccion : bloque
            | llamadoAFunciones PUNTOYCOMA
            | declaroAsigno PUNTOYCOMA
            | asignacion PUNTOYCOMA
            | prototipadoFuncion PUNTOYCOMA
            | desarrolloFuncion
            | retorno PUNTOYCOMA
            | bloqueif
            | bloqueElse
            | bloquefor
            | bloquewhile
            ;
variable:VARIABLE;
numero:NUMERO;
bloque : LLAVEABRE instrucciones LLAVECIERRA;
declaroAsigno : tdato itop;
tdato : TDATO;

asignacion :  itop;
prototipadoFuncion : tdato variable PARENTESISABRE (tdato (variable|numero) (COMA|))* PARENTESISCIERRA;
llamadoAFunciones: variable PARENTESISABRE ((variable|numero) (COMA|))* PARENTESISCIERRA;
desarrolloFuncion: tdato variable PARENTESISABRE (tdato (variable|numero) (COMA|))* PARENTESISCIERRA instruccion;
retorno: 'return' (numero|variable|);
bloqueif: IF PARENTESISABRE (itop) PARENTESISCIERRA instruccion;
bloqueElse: ELSE instruccion;
bloquewhile: WHILE PARENTESISABRE (itop) PARENTESISCIERRA instruccion;
bloquefor: FOR PARENTESISABRE  ((VARIABLE|numero) IGUAL (VARIABLE|numero)) PUNTOYCOMA (VARIABLE (IGUAL|MAYOR|MENOR) (VARIABLE|NUMERO)) PUNTOYCOMA ((VARIABLE (SUMAUNO | RESTAUNO)) | ((SUMAUNO | RESTAUNO) VARIABLE) | (VARIABLE (MASIGUAL | MENOSIGUAL) (VARIABLE|NUMERO))) PARENTESISCIERRA instruccion;
 
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