"""
    Practica 3: Uso de función lambda
    @davisalex22
    
Dada la siguiente llamada a una función anónima:

suma(10,11)

Desarrollar la función; debe presentar en pantalla para el ejemplo 21
"""


suma = (10,11)

num1 = lambda x: x[0] + x[1]

print(num1(suma))

