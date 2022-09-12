grammar compiladores;

fragment LETRA : [A-Za-z] ;
fragment DIGITO : [0-9] ;
PUNTOYCOMA : ';';
COMA : ',';
PUNTO : '.';
LLAVEABRE : '{';
LLAVECIERRA : '}';
CORCHETEABRE : '[';
CORCHETECIERRA : ']';
PARENTESISCIERRA : ')';
PARENTESISABRE : '(';
OP: MAS|MENOS|PRODUCTO|DIVISION;
MAS: '+';
MENOS: '-';
PRODUCTO: '*';
DIVISION: '/';
CONDICIONAL: MENOR|MAYOR|IGUALDAD|NEGACION;
IGUAL : '=';
MENOR : '<';
MAYOR : '>';
IGUALDAD: '==';
NEGACION : '!=';
TDATO :INT
      |STRING
      |FLOAT
      |DOUBLE
      ;
INT: 'int';
STRING: 'string';
FLOAT: 'float';
DOUBLE: 'double';
IF : 'if';
FOR : 'for';
WHILE : 'while';
DO : 'do';
FLOTANTES : DIGITO PUNTO DIGITO;
FLOTANTESNEGATIVOS : '-' DIGITO PUNTO DIGITO;
NUMERO : DIGITO+ ;


VARIABLE : (LETRA | '_')(LETRA | DIGITO | '_')* ;

WS : [ \t\n\r] -> skip;
OTRO : . ;

//Verifico que todos los parentesis se abran y se cierren fragment
//Analisis sintactico descendente ----> Voy de la raiz a las hojas
// antlr4 usa descendente

/*Raiz*///d  si : s EOF;

//s : PARENTESISABRE s PARENTESISCIERRA s
// | CORCHETEABRE s CORCHETECIERRA s
// | LLAVEABRE s LLAVECIERRA s
// |
// ;


prog : instrucciones EOF ;
instrucciones : instruccion instrucciones
              |
              ;

instruccion : bloque
            | declaracion PUNTOYCOMA
            | operacion PUNTOYCOMA
            | asignacion PUNTOYCOMA
            | prototipadoFuncion PUNTOYCOMA
            | llamadoAFunciones PUNTOYCOMA
            | desarrolloFuncion
            | retorno PUNTOYCOMA
            | bloqueif
          //  | bloquefor
          //  | bloquewhile
  //          |
              ;

bloque : LLAVEABRE instrucciones LLAVECIERRA;
declaracion : TDATO (COMA|VARIABLE)+;
asignacion : (TDATO|) (COMA|VARIABLE (IGUAL (NUMERO|VARIABLE|llamadoAFunciones|operacion)))+;
prototipadoFuncion : TDATO VARIABLE PARENTESISABRE (TDATO (VARIABLE|NUMERO) (COMA|))* PARENTESISCIERRA;
llamadoAFunciones: VARIABLE PARENTESISABRE ((VARIABLE|NUMERO) (COMA|))* PARENTESISCIERRA;
desarrolloFuncion: TDATO VARIABLE PARENTESISABRE (TDATO (VARIABLE|NUMERO) (COMA|))* PARENTESISCIERRA instrucciones;
operacion: ( (VARIABLE|NUMERO) OP (VARIABLE|NUMERO));
retorno: 'return' (NUMERO|VARIABLE);
bloqueif: IF PARENTESISABRE ((NUMERO|VARIABLE)CONDICIONAL(NUMERO|VARIABLE)) PARENTESISCIERRA instrucciones;

//bloquewhile: PARENTESISABRE IF PARENTESISCIERRA instruccion;



//Analisis sintactico Ascendente ----> Voy de las hojas a la raiz

//variable, asignar variables, llamado a funciones, prototipado, bucles, if