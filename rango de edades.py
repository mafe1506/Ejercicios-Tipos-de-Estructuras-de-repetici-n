# Algoritmo para contar el número de personas en diferentes rangos de edad
def contar_personas_por_rango_de_edad(edades):
    rangos = {
        "0-20": 0,
        "20-30": 0,
        "30-40": 0,
        "40-60": 0,
        "60+": 0
    }

    for edad in edades:
        if edad <= 20:
            rangos["0-20"] += 1
        elif edad <= 30:
            rangos["20-30"] += 1
        elif edad <= 40:
            rangos["30-40"] += 1
        elif edad <= 60:
            rangos["40-60"] += 1
        else:
            rangos["60+"] += 1

    return rangos

# Proceso de prueba de escritorio
# Supongamos que tenemos las edades de las 10 personas en una lista
edades = [18, 25, 32, 45, 50, 28, 60, 70, 15, 22]

resultados_esperados = {
    "0-20": 2,
    "20-30": 3,
    "30-40": 1,
    "40-60": 3,
    "60+": 1
}

resultados_obtenidos = contar_personas_por_rango_de_edad(edades)

if resultados_obtenidos == resultados_esperados:
    print("Totales por rango de edades:")
    for rango, total in resultados_obtenidos.items():
        print(f"{rango}: {total} personas")
else:
    print("Error: Los resultados obtenidos no coinciden con los resultados esperados.")
