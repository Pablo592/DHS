grammar compiladores;

fragment LETRA : [A-Za-z] ;
fragment DIGITO : [0-9] ;
PUNTOYCOMA : ';';
COMA : ',';
PUNTO : '.';
ESPACIO : ' ';
LLAVEABRE : '{';
LLAVECIERRA : '}';
CORCHETEABRE : '[';
CORCHETECIERRA : ']';
PARENTESISCIERRA : ')';
PARENTESISABRE : '(';
MAS: '+';
MENOS: '-';
PRODUCTO: '*';
DIVISION: '/';
IGUAL : '=';
MENOR : '<';
MAYOR : '>';
IGUALDAD: '==';
NEGACION : '!=';
INT: 'int';
IF : 'if';
FOR : 'for';
WHILE : 'while';
DO : 'do';
FLOTANTES : DIGITO PUNTO DIGITO;
FLOTANTESNEGATIVOS : '-' DIGITO PUNTO DIGITO;
HEXADECIMALES : '0''x' ([a-f]|[A-Z]|DIGITO)+;
NUMERO : DIGITO+ ;
PALABRA : LETRA+;
BYTE : DIGITO | DIGITO DIGITO | '1' ? DIGITO DIGITO | '2' ([0-5] [0-5]);
IP : BYTE PUNTO BYTE PUNTO BYTE PUNTO BYTE;
CORREO: PALABRA '@' (PALABRA PUNTO PALABRA)+;
DOMINIO : PALABRA PUNTO PALABRA*;
WS : [ \t\n\r] -> skip;
OTRO : . ;

ID : (LETRA | '_')(LETRA | DIGITO | '_')+ ;


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
            | declaracion
          //  | asignacion
          //  | bloqueif
          //  | bloquefor
          //  | bloquewhile
  //          |
              ;

bloque : LLAVEABRE instrucciones LLAVECIERRA;

declaracion : tdato ID PUNTOYCOMA;

bloquewhile: PARENTESISABRE IF PARENTESISCIERRA instruccion;

tdato : INT;

//Analisis sintactico Ascendente ----> Voy de las hojas a la raiz




/* 
s : 
  | NUMERO {print("NUMERO ->" + $NUMERO.text + "<--") } s
  | PUNTOYCOMA {print("PUNTOYCOMA ->" + $PUNTOYCOMA.text + "<--") } s
  | COMA {print("COMA ->" + $COMA.text + "<--") } s
  | PUNTO {print("PUNTO ->" + $PUNTO.text + "<--") } s
  | LLAVEABRE {print("LLAVEABRE ->" + $LLAVEABRE.text + "<--") } s
  | LLAVECIERRA {print("LLAVECIERRA ->" + $LLAVECIERRA.text + "<--") } s
  | CORCHETEABRE {print("CORCHETEABRE ->" + $CORCHETEABRE.text + "<--") } s
  | CORCHETECIERRA {print("CORCHETECIERRA ->" + $CORCHETECIERRA.text + "<--") } s
  | PARENTESISCIERRA {print("PARENTESISCIERRA ->" + $PARENTESISCIERRA.text + "<--") } s
  | PARENTESISABRE {print("PARENTESISABRE ->" + $PARENTESISABRE.text + "<--") } s
  | MAS {print("MAS ->" + $MAS.text + "<--") } s
  | MENOS {print("MENOS ->" + $MENOS.text + "<--") } s
  | PRODUCTO {print("PRODUCTO ->" + $PRODUCTO.text + "<--") } s
  | DIVISION {print("DIVISION ->" + $DIVISION.text + "<--") } s
  | IGUAL {print("IGUAL ->" + $IGUAL.text + "<--") } s
  | MENOR {print("MENOR ->" + $MENOR.text + "<--") } s
  | MAYOR {print("MAYOR ->" + $MAYOR.text + "<--") } s
  | IGUALDAD {print("IGUALDAD ->" + $IGUALDAD.text + "<--") } s
  | NEGACION {print("NEGACION ->" + $NEGACION.text + "<--") } s
  | IF {print("IF ->" + $IF.text + "<--") } s
  | FOR {print("FOR ->" + $FOR.text + "<--") } s
  | WHILE {print("WHILE ->" + $WHILE.text + "<--") } s
  | DO {print("DO ->" + $DO.text + "<--") } s
  | FLOTANTES {print("FLOTANTES ->" + $FLOTANTES.text + "<--") } s
  | FLOTANTESNEGATIVOS {print("FLOTANTESNEGATIVOS ->" + $FLOTANTESNEGATIVOS.text + "<--") } s
  | HEXADECIMALES {print("HEXADECIMALES ->" + $HEXADECIMALES.text + "<--") } s
  | PALABRA {print("PALABRA ->" + $PALABRA.text + "<--") } s
  | IP {print("IP ->" + $IP.text + "<--") } s
  | DOMINIO {print("DOMINIO ->" + $DOMINIO.text + "<--") } s
  | CORREO {print("CORREO ->" + $CORREO.text + "<--") } s
  | ESPACIO {print("ESPACIO ->" + $ESPACIO.text + "<--") } s
  | ID     {print("ID ->" + $ID.text + "<--") }         s
  | OTRO   {print("Otro ->" + $OTRO.text + "<--") }     s
  | EOF
  ;

  variable, asignar variables, llamado a funciones, prototipado, bucles, if
  */