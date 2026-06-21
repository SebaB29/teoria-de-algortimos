from problema_4.problema_4 import *

INTENTOS = 1000
ELEMENTOS_TABLA = 10000

# Grafo de prueba
Grafo = {
    1: [2, 3, 4],
    2: [1, 3, 5],
    3: [1, 2, 4, 5, 6],
    4: [1, 3, 6],
    5: [2, 3, 6],
    6: [3, 4, 5]
}


def generar_promedio():
    cantidades_aristas = []

    # Veo cual es la media de la cantidad de aristas satsifechas para 1000 intentos
    for _ in range(INTENTOS):
        satisfechas = calcular_aristas_satisfechas(Grafo)
        cantidades_aristas.append(satisfechas)

    cantidad_aristas_satisfechas = 0
    for cantidad in cantidades_aristas:
        cantidad_aristas_satisfechas += cantidad

    promedio = cantidad_aristas_satisfechas / INTENTOS

    return promedio


def generar_archivo_promedios():
    file_path = "promedios_obtenidos.csv"  # El path es la raiz del pryecto

    with open(file=file_path, mode='w') as file:
        # Registro en un archvio 10000 intentos de promedios obtenidos
        file.write("Intento, Promedio\n")
        for i in range(ELEMENTOS_TABLA):
            promedio = generar_promedio()
            file.write(f"{i},{promedio}\n")

    print("Archivo generado.")


generar_archivo_promedios()
