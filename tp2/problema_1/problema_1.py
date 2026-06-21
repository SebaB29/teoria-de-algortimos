import sys
import csv
import time
import os
from pulp import LpProblem, LpMaximize, LpVariable, lpSum, LpBinary, LpStatus, value, PULP_CBC_CMD

def cargar_archivo(ruta):
    """Carga las ofertas y retorna un diccionario con los datos."""
    ofertas = {}
    try:
        with open(ruta, "r") as archivo:
            for linea in archivo:
                valores = linea.replace(',', ' ').split()
                if len(valores) < 4:
                    continue
                clave = (valores[0].strip(), valores[1].strip())
                ofertas[clave] = {
                    "valor": int(valores[2].strip()),
                    "cantidad": int(valores[3].strip())
                }
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta}", file=sys.stderr)
        sys.exit(1)
        
    return ofertas

def resolver_modelo(dict_ofertas, ruta_modelo):
    """
    Define y resuelve el modelo de programación lineal.
    Retorna un diccionario con los resultados matemáticos puros.
    """
    prob = LpProblem("Maximizacion_Beneficios_Publicidad", LpMaximize)
    indices = list(dict_ofertas.keys())

    # Variables de decisión
    Y = LpVariable.dicts("Oferta", indices, cat=LpBinary)
    
    # Función objetivo
    prob += lpSum(Y[i] * dict_ofertas[i]["valor"] for i in indices), "Beneficio_Total"
    
    # Restricciones
    # 1. Solo se puede aceptar una oferta del cliente B (B = 1)
    prob += (lpSum(Y[i] for i in indices if i[0] == "B")) <= 1 
    # 2. Solo se pueden aceptar la oferta del cliente A o del cliente D, no ambas
    prob += (lpSum(Y[i] for i in indices if i[0] == "A") + lpSum(Y[i] for i in indices if i[0] == "D")) <= 1
    # 3. la cantidad de paradas vendidas no puede ser mayor a 200
    prob += lpSum(Y[i] * dict_ofertas[i]["cantidad"] for i in indices) <= 200

    # Asegurar que exista la carpeta 'model' antes de guardar
    os.makedirs(os.path.dirname(ruta_modelo), exist_ok=True)
    prob.writeLP(ruta_modelo)
    
    # Resolución silenciosa (msg=False evita que PuLP ensucie la consola)
    start_time = time.perf_counter()
    status = prob.solve(PULP_CBC_CMD(msg=False))
    end_time = time.perf_counter()
    
    # Empaquetar resultados
    resultados = {
        "estado": LpStatus[status],
        "tiempo_ejecucion": end_time - start_time,
        "maximo": 0,
        "paradas_totales": 0,
        "ofertas_aceptadas": []
    }
    
    if LpStatus[status] == "Optimal":
        resultados["maximo"] = value(prob.objective)
        for i in indices:
            if Y[i].varValue == 1:
                resultados["ofertas_aceptadas"].append({
                    "cliente": i[0],
                    "oferta": i[1],
                    "valor": dict_ofertas[i]["valor"],
                    "cantidad": dict_ofertas[i]["cantidad"]
                })
                resultados["paradas_totales"] += dict_ofertas[i]["cantidad"]
                
    return resultados

def main():
    # 1. Recepción de argumentos
    if len(sys.argv) != 2:
        print("Uso: python3 problema_1_pl.py <archivo_entrada>")
        sys.exit(1)
        
    ruta_entrada = sys.argv[1]
    
    # 2. Generación dinámica de la ruta del modelo (.lp)
    nombre_base = os.path.splitext(os.path.basename(ruta_entrada))[0]
    ruta_modelo = os.path.join("model", f"modelo_{nombre_base}.lp")
    
    # 3. Lógica pura
    datos = cargar_archivo(ruta_entrada)
    resultados = resolver_modelo(datos, ruta_modelo)
    
    # 4. Impresión por pantalla (stdout) para que Bash lo capture
    print(f"Archivo procesado: {os.path.basename(ruta_entrada)}")
    print(f"Estado de la solucion: {resultados['estado']}")
    print("-" * 50)
    
    if resultados['estado'] == "Optimal":
        print("Ofertas aceptadas:")
        for of in resultados['ofertas_aceptadas']:
            print(f" - Cliente: {of['cliente']} | Oferta: {of['oferta']} | Valor: USD {of['valor']} | Paradas: {of['cantidad']}")
        print("-" * 50)
        print(f"Beneficio Maximo Obtenido: USD {resultados['maximo']}")
        print(f"Cantidad total de paradas: {resultados['paradas_totales']} / 200")
        
    print(f"Tiempo de ejecucion: {resultados['tiempo_ejecucion']:.6f} segundos")

if __name__ == '__main__':
    main()