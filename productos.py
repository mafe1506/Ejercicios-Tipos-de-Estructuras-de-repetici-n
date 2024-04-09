# Algoritmo para calcular el costo total de 10 productos y mostrar el precio antes y después del IVA
def calcular_costo_total():
    productos = []
    for i in range(1, 11):
        precio = float(input(f"Ingrese el precio del producto {i}: "))
        productos.append(precio)

    costo_total_antes_iva = sum(productos)
    costo_total_despues_iva = costo_total_antes_iva * 1.16  # Calculando el precio después del IVA

    print(f"El costo total antes de IVA es: ${costo_total_antes_iva:.2f}")
    print(f"El costo total después de IVA es: ${costo_total_despues_iva:.2f}")

# Llamando a la función para calcular el costo total
calcular_costo_total()
