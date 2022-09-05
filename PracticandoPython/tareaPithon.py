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

textoGrande = str(input("Ingrese un string grande: "))

textoRepitente = str(input("Ingrese un string pequeño: "))

print('La cantidad de veces que se repite es de:', textoGrande.count(textoRepitente))

#Ejercicio 8

