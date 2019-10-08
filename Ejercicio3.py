"""
    Ejemplo 3: Uso de función lambda
    @davisalex22

"""
# Cada elemento de datos, tiene (edad y estatura)

datos = ((30 , 1.79) ,  (25, 1.60) , (35, 1.68))

dato = lambda x: x[2]

print(dato(datos))
