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
CONDICIONAL: MENOR | MAYOR | IGUALDAD | DISTINTO;
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
INT: 'int';
STRING: 'string';
FLOAT: 'float';
DOUBLE: 'double';
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



/* 
itop : oparit itop
     |
     ;
oparit : exp ;

exp : term t ;

t : MAS term t
  |
  ;

term : factor f ;

f : PRODUCTO factor f
  |
  ;

factor : VARIABLE
       | NUMERO
       | PARENTESISABRE exp PARENTESISCIERRA
       ;
*/











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

pi: pu sumoResto;

sumoResto:MAS pu sumoResto
         |MENOS pu sumoResto
         |
         ;

pu: pe multiDivi;

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
       
  /*  
prog: instrucciones EOF;
instrucciones: instruccion instrucciones |;

instruccion:
	bloque
	| llamadoAFunciones PUNTOYCOMA
	| declaracion PUNTOYCOMA
	| asignacion PUNTOYCOMA
	| prototipadoFuncion PUNTOYCOMA
	| desarrolloFuncion
	| retorno PUNTOYCOMA
	| bloqueif
	| bloquefor
	| bloquewhile;

bloque: LLAVEABRE instrucciones LLAVECIERRA;
declaracion: tipoDato (COMA | VARIABLE)+;
asignacion: (tipoDato |) (COMA| (VARIABLE ((IGUAL (NUMERO| VARIABLE| llamadoAFunciones |operacion))| SUMAUNO)))+;
prototipadoFuncion: tipoDato VARIABLE PARENTESISABRE (tipoDato (VARIABLE | NUMERO) (COMA |))* PARENTESISCIERRA;
llamadoAFunciones:VARIABLE PARENTESISABRE ((VARIABLE | NUMERO) (COMA |))* PARENTESISCIERRA;
desarrolloFuncion:tipoDato VARIABLE PARENTESISABRE (tipoDato (VARIABLE | NUMERO) (COMA |))* PARENTESISCIERRA instrucciones;
retorno: 'return' (NUMERO | VARIABLE);
bloqueif:IF PARENTESISABRE (((NUMERO | VARIABLE) CONDICIONAL (NUMERO | VARIABLE))| BOOLEANOS) PARENTESISCIERRA instrucciones ((ELSE instrucciones) |);
bloquewhile:WHILE PARENTESISABRE (((NUMERO | VARIABLE) CONDICIONAL (NUMERO | VARIABLE))| BOOLEANOS) PARENTESISCIERRA instrucciones;
bloquefor: FOR PARENTESISABRE (asignacion)* PUNTOYCOMA (((NUMERO | VARIABLE) CONDICIONAL (NUMERO | VARIABLE))*| BOOLEANOS) PUNTOYCOMA (asignacion )* PARENTESISCIERRA instrucciones;
*/  
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