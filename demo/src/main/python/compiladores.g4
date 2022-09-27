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
OTRO: .;

/*
 //Verifico que todos los parentesis se abran y se cierren fragment //Analisis sintactico
 descendente ----> Voy de la raiz a las hojas // antlr4 usa descendente
 
 Raiz//d si : s EOF;
 
 //s : PARENTESISABRE s PARENTESISCIERRA s // | CORCHETEABRE s CORCHETECIERRA s // | LLAVEABRE s
 LLAVECIERRA s // | // ;
 */


itop : oparit itop
     |
     ;
// c = a + b + d + f / r * q
oparit : expo;

expo : tie coma;

coma: COMA
    |
    ;

tie : to igualOperaciones;

igualOperaciones:IGUAL
                |PRODUCTOIGUAL
                |DIVIDIDOIGUAL
                |RESTOIGUAL
                |MASIGUAL
                |MENOSIGUAL
                |
                ;
         

to: ti orLogico;

orLogico: OR
        |
        ;

ti: te andLogico;

andLogico: AND
         |
         ;

te: po igualo;

igualo:IGUALDAD
      |DISTINTO
      |
      ;

po: pi relaciono;

relaciono:MAYOR
         |MENOR
         |MAYORIGUAL
         |MENORIGUAL
         |
         ;

pi: pu sumoResto;

sumoResto:MAS
         |MENOS
         |
         ;

pu: pe multiDivi;

multiDivi:PRODUCTO
         |DIVISION
         |RESTO
         |
         ;

pe: pa tipoDato;

tipoDato:INT
        |STRING
        |FLOAT
        |DOUBLE
        |
        ;

pa: factor prefijo;

prefijo:RESTAUNO VARIABLE
       |SUMAUNO VARIABLE
       |NEGACION
       |
       ;

factor: VARIABLE
       |tipoDato VARIABLE
       |PUNTO
       |NUMERO
       |CORCHETEABRE (VARIABLE|NUMERO) CORCHETECIERRA
       |PARENTESISABRE itop PARENTESISCIERRA
       ;
       
prog: instrucciones EOF;
instrucciones: instruccion instrucciones |;

instruccion:
	bloque
	| llamadoAFunciones PUNTOYCOMA
	| declaracion PUNTOYCOMA
	//   | operacion PUNTOYCOMA
	| asignacion PUNTOYCOMA
	| prototipadoFuncion PUNTOYCOMA
	| desarrolloFuncion
	| retorno PUNTOYCOMA
	| bloqueif
	| bloquefor
	| bloquewhile;

bloque: LLAVEABRE instrucciones LLAVECIERRA;
declaracion: tipoDato (COMA | VARIABLE)+;
asignacion: (tipoDato |) (COMA| (VARIABLE ((IGUAL (NUMERO| VARIABLE| llamadoAFunciones /*|operacion*/))| SUMAUNO)))+;
prototipadoFuncion: tipoDato VARIABLE PARENTESISABRE (tipoDato (VARIABLE | NUMERO) (COMA |))* PARENTESISCIERRA;
llamadoAFunciones:VARIABLE PARENTESISABRE ((VARIABLE | NUMERO) (COMA |))* PARENTESISCIERRA;
desarrolloFuncion:tipoDato VARIABLE PARENTESISABRE (tipoDato (VARIABLE | NUMERO) (COMA |))* PARENTESISCIERRA instrucciones;
//operacion: ( (VARIABLE|NUMERO) OP (VARIABLE|NUMERO));
retorno: 'return' (NUMERO | VARIABLE);
bloqueif:IF PARENTESISABRE (((NUMERO | VARIABLE) CONDICIONAL (NUMERO | VARIABLE))| BOOLEANOS) PARENTESISCIERRA instrucciones ((ELSE instrucciones) |);
bloquewhile:WHILE PARENTESISABRE (((NUMERO | VARIABLE) CONDICIONAL (NUMERO | VARIABLE))| BOOLEANOS) PARENTESISCIERRA instrucciones;
bloquefor: FOR PARENTESISABRE (asignacion)* PUNTOYCOMA (((NUMERO | VARIABLE) CONDICIONAL (NUMERO | VARIABLE))*| BOOLEANOS) PUNTOYCOMA (asignacion /*|OP*/)* PARENTESISCIERRA instrucciones;

//bloquewhile: PARENTESISABRE IF PARENTESISCIERRA instruccion;

//Analisis sintactico Ascendente ----> Voy de las hojas a la raiz

//variable, asignar variables, llamado a funciones, prototipado, bucles, if

// bloquewhile : PA comparacion/opal PC instruccion ;