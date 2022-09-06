#   1. Python como calculadora

#Ejercicio 1
'''
a = 10;
b = 300;

if (a*b > 10000):
    print("suma a + b = ",a+b)
else:
    print("Producto a*b = ",a*b)
'''
#Ejercicio 2
'''

import math


dinero = [1000,500,200,100,10,5,2,1]
billetera = [0]*10001

monto = int(input("Ingrese el monto: "))

for i in dinero:
    if monto == 0:
        break
    if(monto >= i):
        aux = math.trunc(monto /i)
        monto -= aux*i
        billetera[i]+=aux

suma = 0

for i in dinero:
    suma += billetera[i]*i
    if(i >= 100):
        print(billetera[i], "billetes de ",i, " pesos", suma)
    else:
          print(billetera[i], "monedas de ",i, " pesos", suma)
'''
#Ejercicio 3

'''
import math
from random import random

matriz = [0] * 5


for i in range(0,len(matriz)):
    num1 = math.trunc(random()*10)
    num2 = math.trunc(random()*10)
    matriz[i] = [num1,num2]


for i in matriz:
    for j in i:
        print(j,"\t")
    print("\n")


print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")

primerPunto = matriz[0]
distanciaMin = 1000;
puntoCerca = [0,0]
for i in range(1,len(matriz)):
    puntoCercano = matriz[i]
    distancia = (abs(primerPunto[0]-puntoCercano[0])**2+abs(primerPunto[1]-puntoCercano[1])**2)**(1/2)
    print(puntoCercano," ", distancia, "\n")
    if(distancia < distanciaMin):
        distanciaMin = distancia
        puntoCerca = matriz[i]


print("Primer punto ",primerPunto,"\n")
print("Punto cercano ",puntoCerca)
'''

#Ejercicio 4

'''
import math
from random import random

lista = [0]*10

for i in range(0,10):
    lista[i] = math.trunc(random()*100)

renglon = ""

for i in range(0,10):
   renglon += str(lista[i]) + " "

print(renglon)
print("\n")

for i in range(0,len(lista)):
    if(i>0):
        print("Numero Anterior: ", lista[i-1])
    print("Numero Actual: ", lista[i])
    if(i< len(lista)-1):
        print("Numero Siguiente: ", lista[i+1])
    else:
        break
    print("\n")
'''

#   2. Strings

#Ejercicio 1

'''
elString = "efwefeferfsefwaesfefgwergwesgwsegse"

for i in range(0,len(elString)):
    if(i*2 <= len(elString)):
        print(elString[i*2])
    else:
        break
'''
#Ejercicio 2

'''
texto = str(input("Ingrese un string: "))
index = int(input("Ingrese un numero entero: "))

substring = texto[:index]
print(substring)
'''
#Ejercicio 3

'''
texto = str(input("Ingrese un string: "))
indexIni = int(input("Ingrese el numero inicial: "))
indexFin = int(input("Ingrese el numero final: "))


substring = texto[indexIni:indexFin]
print(substring)
'''

#Ejercicio 4

'''
texto = str(input("Ingrese un numero: "))
substring = ""

for i in range(0,len(texto)):
    if((len(texto))-i) > 0:
        substring +=texto[(len(texto)-1)-i:len(texto)-i]

print(substring)

'''
#Ejercicio 5

'''
mayusculas = 0
minusculas = 0
simbolos = 0

texto = str(input("Ingrese un string: "))

for i in texto:
    if(((ord(i)>= ord('A')) &( ord(i)<= ord('Z')))|((ord(i)>= ord('a')) & (ord(i)<= ord('z')))):
        if(i == i.lower()):
            minusculas+=1
        else:
            mayusculas+=1
    else:
        simbolos+=1

print(ord('a'))
print(ord('z'))

print("Hay ",mayusculas, " mayusculas ",minusculas," minusculas y",simbolos," simbolos")
'''
#Ejercicio 6 y 7

'''
textoGrande = str(input("Ingrese un string grande: "))

textoRepitente = str(input("Ingrese un string pequeño: "))

print('La cantidad de veces que se repite es de:', textoGrande.count(textoRepitente))
'''

#Ejercicio 10

'''
from difflib import SequenceMatcher as SM


texto1 = str(input("Ingrese un string: "))
texto2 = str(input("Ingrese otro string: "))

print(SM(None, texto1, texto2).ratio())
'''
#Ejercicio 11

'''
texto = str(input("Ingrese una palabra: "))

for i in range(0,len(texto)):
    if(texto[i] != texto[len(texto)-1 - i]):
        print("No es palindroma")
        break
    if(0 == (len(texto)-1 - i)):
        print("Si es palindroma")
        break
'''

#Ejercicio 14

'''
texto = str(input("Ingrese un string: "))

suma = 0
numero = ""

for i in texto:
     if((ord(i)>= ord('0')) & (ord(i)<= ord('9'))):
        numero+=i
     else: 
        if(numero != ""):
            suma+=int(numero)
            numero = ""

print("La suma es: ",suma)
'''

#Ejercicio 15

'''
correo = str(input("Ingrese un correo: "))
contrasenia = str(input("Ingrese una contraseña: "))

if not "." in correo:
    print("Correo incorrecto")
else:
    if not "@" in correo:
        print("Correo incorrecto")
    else:
        print("Correo correcto")

mayus = 0
minus = 0
simbol = 0

for i in contrasenia:
    if(((ord(i)>= ord('A')) &( ord(i)<= ord('Z')))|((ord(i)>= ord('a')) & (ord(i)<= ord('z')))):
        if(i == i.lower()):
            minus = 1
        else:
            mayus = 1
    else:
        simbol = 1

if (minus + mayus + simbol) >= 2:
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")

'''

#   3. Listas

#Ejercicio 1

'''
import math
from random import random

lista1 = [0]*101
lista2 = [0]*101


for i in range(0,100):
    lista1[i] = math.trunc(random()*100)
    lista2[i] = math.trunc(random()*100)


print("Numeros de la lista 1 divisibles por 5")
for i in range(0,100):
    if(lista1[i]%5 == 0):
        print(lista1[i])


print("Numeros de la lista 2 divisibles por 5")
for i in range(0,100):
    if(lista2[i]%5 == 0):
        print(lista2[i])

suma = 0

print("Suma vectorial de la lista 1")
for i in lista1:
    suma+=i
print(suma)
suma = 0

print("Suma vectorial de la lista 2")
for i in lista2:
    suma+=i
print(suma)


print("Producto punto")
suma = 0
for i in range(0,100):
    suma+= lista1[i]*lista2[i]

print(suma)
'''

#Ejercicio 2

'''
import math
from random import random

lista1 = [0]*101


for i in range(0,100):
    lista1[i] = math.trunc(random()*100)


print("Numeros pares")
for i in range(0,100):
    if(lista1[i]%2 == 0):
        print(lista1[i])


print("Numeros impares")
for i in range(0,100):
    if(lista1[i]%2 != 0):
        print(lista1[i])
'''

#Ejercicio 3

'''
mayusculas = ""
minusculas = ""
simbolos = ""

texto = str(input("Ingrese un string: "))

for i in texto:
    if(((ord(i)>= ord('A')) &( ord(i)<= ord('Z')))|((ord(i)>= ord('a')) & (ord(i)<= ord('z')))):
        if(i == i.lower()):
            minusculas+=i
        else:
            mayusculas+=i

print("Mayusculas: ",mayusculas, " Minusculas ",minusculas)
'''

#Ejercicio 4

'''
import math
from random import random

lista1 = [0]*101

for i in range(0,100):
    lista1[i] = (math.trunc(random()*100))*((-1)**int(random()*3))
    if(lista1[i] < 0):
        print(0)
    else:
        print(lista1[i])
'''

#Ejercicio 5

'''
import math
from random import random
import numpy as np


matriz1 = [0] * 3
matriz2 = [0] * 3

matrizResultado = [0]*3

for i in range(0,len(matrizResultado)):
    matriz1[i] = [0]*3


for i in range(0,len(matriz1)):
    matriz1[i] = [math.trunc(random()*10),math.trunc(random()*10),math.trunc(random()*10)]
    matriz2[i] = [math.trunc(random()*10),math.trunc(random()*10),math.trunc(random()*10)]


matrizResultado = np.dot(matriz1,matriz2)

for i in matrizResultado:
    print(i,"\t")
    print("\n")
'''

#Ejercicio 6 y 7

'''
import math
from random import random

lista = [999]*100
listaResultante = [999]*100

for i in range(0,len(lista)):
    lista[i] = math.trunc(random()*100)


for i in lista:
    listaResultante[i]=i

j = 0
for i in listaResultante:
    if(i < 999):
        lista[j] = i
        j+=1

i = 0
listaResultante = [0]*j

while(i<j):
    listaResultante[i] = lista[i]
    i+=1

for i in listaResultante:
    print(i)
'''

#   4. Diccionarios

#Ejercicio 1

'''
diccionario = {
     "Diez":10,
     "Veinte":20,
     "Treinta":30
 }

print(diccionario.items())
'''
#Ejercicio 2

'''
diccionario = {
     "Diez":10,
     "Veinte":20,
     "Treinta":30
 }


diccionario.setdefault('Cuarenta',40)

print(diccionario.items())
'''
#Ejercicio 3
'''

diccionario = {
     "Diez":10,
     "Veinte":20,
     "Treinta":30
 }


diccionario.setdefault('Cuarenta',40)
diccionario.pop("Veinte")
print(diccionario.items())
'''

#Ejercicio 4

'''
estudiante = {
     "Nombre":'Pedro',
     "Apellido":'Sanchez',
     "Legajo":'wdwdwdwdwd',
     "Materias":['Fisica','Quimica']
 }

print(estudiante.items())
'''

#Ejercicio 5

'''
estudiante = {
     "Nombre":'Pedro',
     "Apellido":'Sanchez',
     "Legajo":'wdwdwdwdwd',
     "Materias":['Fisica','Quimica']
 }

legajo = str(input("Ingrese el legajo: "))

estudiante['Legajo'] =legajo

materia1 = [str(input("Ingrese la materia 1: "))]

materia2 = [str(input("Ingrese la materia 2: "))]

materias = estudiante.get("Materias")+(materia1)+(materia2)
estudiante['Materias']=materias

print(estudiante.items())
'''

#Ejercicio 6

'''
import math
from random import random

estudiante = {
     "Nombre":'Pedro',
     "Apellido":'Sanchez',
     "Legajo":'wdwdwdwdwd',
     "Materias":['Fisica','Quimica']
 }

legajo = str(input("Ingrese el legajo: "))

estudiante['Legajo'] =legajo

materia1 = [str(input("Ingrese la materia 1: "))]

materia2 = [str(input("Ingrese la materia 2: "))]

materias = estudiante.get("Materias")+(materia1)+(materia2)
estudiante['Materias']=materias

materia = [{
    "Nombre":"",
    "Codigo":""
},{
    "Nombre":"",
    "Codigo":""
},{
    "Nombre":"",
    "Codigo":""
},{
    "Nombre":"",
    "Codigo":""
}]

j = 0


for i in estudiante.get("Materias"):
    
    materia[j]['Nombre'] = i
    materia[j]['Codigo'] = math.trunc(random()*100)
    j+=1

estudiante['Materias']=materia
print(estudiante.items())
'''

#Ejercicio 7

'''
import math
from random import random

estudiante = {
     "Nombre":'Pedro',
     "Apellido":'Sanchez',
     "Legajo":'wdwdwdwdwd',
     "Materias":['Fisica','Quimica']
 }

legajo = str(input("Ingrese el legajo: "))

estudiante['Legajo'] =legajo

materia1 = [str(input("Ingrese la materia 1: "))]

materia2 = [str(input("Ingrese la materia 2: "))]

materias = estudiante.get("Materias")+(materia1)+(materia2)
estudiante['Materias']=materias

materia = [{
    "Nombre":"",
    "Codigo":""
},{
    "Nombre":"",
    "Codigo":""
},{
    "Nombre":"",
    "Codigo":""
},{
    "Nombre":"",
    "Codigo":""
}]

j = 0


for i in estudiante.get("Materias"):
    
    materia[j]['Nombre'] = i
    materia[j]['Codigo'] = math.trunc(random()*100)
    j+=1

estudiante['Materias']=materia
print(estudiante.items())

estDiez = [estudiante]*10

for i in estDiez:
    print(i.items())
'''