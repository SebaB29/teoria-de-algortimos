import sys
import time

def subconjunto_factible_aprox(A: list, B: int) -> list:
    """
    Algoritmo de aproximación (Greedy ordenado).
    Garantiza una solución >= OPT/2.
    Complejidad Temporal: O(n log n)
    """
    # 1. Preprocesamiento: Ordenar de mayor a menor
    A_ordenado = sorted(A, reverse=True)
    
    S = []
    T = 0
    
    # 2. Procesamiento greedy
    for elemento in A_ordenado:
        if T + elemento <= B:
            S.append(elemento)
            T += elemento
            
    return S

def main():
    # Validación de argumentos
    if len(sys.argv) != 2:
        print("Uso: python problema_3.py <ruta_al_archivo_de_prueba.txt>")
        sys.exit(1)
        
    ruta_archivo = sys.argv[1]
    
    try:
        # Lectura del archivo de prueba
        with open(ruta_archivo, 'r') as f:
            lineas = f.readlines()
            
        # Asumimos formato: Línea 1 = B, Línea 2 = Elementos de A
        B = int(lineas[0].strip())
        
        # Soportamos elementos separados por espacios o comas
        valores = lineas[1].replace(',', ' ').split()
        A = [int(v) for v in valores]
        
        # Ejecución y medición simple
        inicio = time.perf_counter()
        solucion = subconjunto_factible_aprox(A, B)
        fin = time.perf_counter()
        
        suma_total = sum(solucion)
        tiempo_ms = (fin - inicio) * 1000
        
        # Salida estándar
        print(f"Archivo procesado: {ruta_archivo}")
        print(f"Cota B: {B} | Elementos evaluados (n): {len(A)}")
        print(f"Suma obtenida: {suma_total}")
        print(f"Tiempo de ejecución: {tiempo_ms:.4f} ms")
        
    except Exception as e:
        print(f"Error procesando {ruta_archivo}: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()