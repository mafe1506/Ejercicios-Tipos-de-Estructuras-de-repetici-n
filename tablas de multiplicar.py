# Algoritmo para generar las tablas de multiplicar del 1 al 100 de un número ingresado por el usuario
def tablas_de_multiplicar(numero):
    for i in range(1, 101):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Proceso de prueba de escritorio
# Supongamos que el usuario ingresa el número 7
numero_ingresado_por_usuario = 7

print(f"Tablas de multiplicar del {numero_ingresado_por_usuario}:")
tablas_de_multiplicar(numero_ingresado_por_usuario)