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
CONDICIONAL: MENOR | MAYOR | IGUALDAD | DISTINTO;
IGUAL: '=';
MENOR: '<';
MAYOR: '>';
IGUALDAD: '==';
AND : '&&';
OR : '||';
DISTINTO: '!=';
SUMAUNO: '++';
RESTAUNO: '--';
TDATO: INT | STRING | FLOAT | DOUBLE;
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

itop :  operation itop
        |
        ;

operation : expression ;

expression : logicOr lor ;

logicOr : logicAnd land;

lor:OR logicOr lor
    |
    ;

logicAnd: term t;

land :  AND logicAnd land
        |
        ;

term : factor f ;

t : MAS term t
   | MENOS term t
   |
  ;

factor : VARIABLE
       | NUMERO
       | PARENTESISABRE expression PARENTESISCIERRA
       ;

f : PRODUCTO factor f
   | DIVISION factor f
   |
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
declaracion: TDATO (COMA | VARIABLE)+;
asignacion: (TDATO |) (COMA| (VARIABLE ((IGUAL (NUMERO| VARIABLE| llamadoAFunciones /*|operacion*/))| SUMAUNO)))+;
prototipadoFuncion: TDATO VARIABLE PARENTESISABRE (TDATO (VARIABLE | NUMERO) (COMA |))* PARENTESISCIERRA;
llamadoAFunciones:VARIABLE PARENTESISABRE ((VARIABLE | NUMERO) (COMA |))* PARENTESISCIERRA;
desarrolloFuncion:TDATO VARIABLE PARENTESISABRE (TDATO (VARIABLE | NUMERO) (COMA |))* PARENTESISCIERRA instrucciones;
//operacion: ( (VARIABLE|NUMERO) OP (VARIABLE|NUMERO));
retorno: 'return' (NUMERO | VARIABLE);
bloqueif:IF PARENTESISABRE (((NUMERO | VARIABLE) CONDICIONAL (NUMERO | VARIABLE))| BOOLEANOS) PARENTESISCIERRA instrucciones ((ELSE instrucciones) |);
bloquewhile:WHILE PARENTESISABRE (((NUMERO | VARIABLE) CONDICIONAL (NUMERO | VARIABLE))| BOOLEANOS) PARENTESISCIERRA instrucciones;
bloquefor: FOR PARENTESISABRE (asignacion)* PUNTOYCOMA (((NUMERO | VARIABLE) CONDICIONAL (NUMERO | VARIABLE))*| BOOLEANOS) PUNTOYCOMA (asignacion /*|OP*/)* PARENTESISCIERRA instrucciones;

//bloquewhile: PARENTESISABRE IF PARENTESISCIERRA instruccion;

//Analisis sintactico Ascendente ----> Voy de las hojas a la raiz

//variable, asignar variables, llamado a funciones, prototipado, bucles, if

// bloquewhile : PA comparacion/opal PC instruccion ;