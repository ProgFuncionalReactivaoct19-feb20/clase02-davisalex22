"""
    Practica 1: Uso de función lambda
    @davisalex22
    
    Desarrollar la función anónima que retorne True or False si el número dado es par.

Ejemplo de llamada

print(valor_par(2))
print(valor_par(3))
print(valor_par(11))

"""


valor_par = lambda num : num %2 == 0

print(valor_par(2))

print(valor_par(3))

print(valor_par(11))