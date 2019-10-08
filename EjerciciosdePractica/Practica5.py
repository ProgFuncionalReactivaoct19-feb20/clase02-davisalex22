"""
    Practica 5: Uso de función lambda
    @davisalex22
    
Dada la siguiente estructura de datos

[(10,2), (8,7), (5,4), (3,11), (10,11)]

Use:
Función map
Dos funciones anónimas
que permita presentar en otra lista; para las primeras posiciones la raiz cuadrada, para las segundas posiciones el cuadrado del número
"""
import math

datos = [(10,2), (8,7), (5,4), (3,11), (10,11)]

 
num1 = lambda x: x[0]

num2 = lambda x: x[1]

funcion =  lambda x: (math.sqrt(num1(x)), num2(x)**2)

print(list(map(funcion, datos)))