"""
    Ejemplo 6: Uso de función lambda
    @davisalex22

"""
# Cada elemento de datos, tiene (edad y estatura)

datos = (
        (30 , 1.79) ,
        (25 , 1.60) ,
        (35 , 1.68))
 
anios = lambda x : x[0]
estatura = lambda x: x[1]

funciones = lambda x: (anios(x)/12.0 , estatura(x)/100)

print(list(map(funciones, datos)))