"""
    Practica 2: Uso de función lambda
    @davisalex22
    
Desarrollar una función anónima que permita retornar la siguiente salida, ejemplo:

CUENCA capital de AZUAY

La llamada a la función es

print(cadena_personalizada("Cuenca", "Azuay"))

"""

cadena_personalizada = lambda x , y: "%s capital de %s" % (x.upper(),y.upper())

print(cadena_personalizada("Cuenca", "Azuay"))
