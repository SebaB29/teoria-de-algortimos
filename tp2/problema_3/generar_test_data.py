import os
import random

def generar_datasets():
    carpeta = "test_data"
    os.makedirs(carpeta, exist_ok=True)
    random.seed(42)

    print("Generando sets de datos...")

    with open(os.path.join(carpeta, "00_contraejemplo.txt"), "w") as f:
        f.write("10\n")       # Cota B
        f.write("3 9 1\n")    # Elementos de A
    print(" - Creado: 00_contraejemplo.txt (n=3)")

    tamanos = [100, 500, 1000, 5000, 10000, 50000]
    for n in tamanos:
        A = [random.randint(1, 1000) for _ in range(n)]

        # Definimos B como el 40% de la suma total de los elementos
        suma_total = sum(A)
        B = int(suma_total * 0.40)

        nombre_archivo = f"{n}.txt"
        ruta = os.path.join(carpeta, nombre_archivo)
        
        # Formateamos el archivo: 
        # Línea 1 = B, 
        # Línea 2 = Elementos de A separados por espacios
        with open(ruta, "w") as f:
            f.write(f"{B}\n")
            f.write(" ".join(map(str, A)) + "\n")
            
        print(f" - Creado: {nombre_archivo} (n={n}, B={B})")

    print("Generación de datasets completada.")

if __name__ == "__main__":
    generar_datasets()