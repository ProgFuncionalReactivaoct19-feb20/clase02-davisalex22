"""
    Practica 4: Uso de función lambda
    @davisalex22
    
Dada la siguiente estructura de datos

[10,2,8,7,5,4,3,11,0, 1]

Use:
Función map
Una función anónima
que permita presentar en otra lista, cada elemento elevado a la tercera potencia.
"""

datos = [10,2,8,7,5,4,3,11,0, 1]

 
num = lambda x: x**3


print(list(map(num, datos)))