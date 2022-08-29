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
OP : [-+*/];
OPREL : [=<>];
IGUALDAD: '==';
NEGACION : '!=';
IF : 'if';
FOR : 'for';
WHILE : 'while';
DO : 'do';
FLOTANTES : DIGITO PUNTO DIGITO;
FLOTANTESNEGATIVOS : '-' DIGITO PUNTO DIGITO;
HEXADECIMALES : '0''x' ([a-f]|[A-Z]|DIGITO)*;
NUMERO : DIGITO+ ;
PALABRA : LETRA+;
IP : NUMERO PUNTO NUMERO PUNTO NUMERO PUNTO NUMERO;
DOMINIO : PALABRA PUNTO PALABRA*;
CORREO: PALABRA '@' (PALABRA PUNTO PALABRA)+;
OTRO : . ;

ID : (LETRA | '_')(LETRA | DIGITO | '_')+ ;




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
  | OP {print("OP ->" + $OP.text + "<--") } s
  | OPREL {print("OPREL ->" + $OPREL.text + "<--") } s
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
  | ID     {print("ID ->" + $ID.text + "<--") }         s
  | OTRO   {print("Otro ->" + $OTRO.text + "<--") }     s
  | EOF
  ;