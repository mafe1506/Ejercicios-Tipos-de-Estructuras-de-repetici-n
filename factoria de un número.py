# Algoritmo para calcular el factorial de un número
def factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

# Proceso de prueba de escritorio
# Supongamos que queremos calcular el factorial de 5
numero_ingresado_por_usuario = 5

factorial_de_numero = factorial(numero_ingresado_por_usuario)
print(f"El factorial de {numero_ingresado_por_usuario} es: {factorial_de_numero}")
