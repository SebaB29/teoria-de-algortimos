import networkx as nx

def buscar_conjuntos_backup(n, d, D, b, k):
    """
    Encuentra el conjunto de backup para cada antena utilizando Edmonds-Karp.

    Parametros:
    n (int): Cantidad de antenas.
    d (list of list): Matriz de distancias de n x n.
    D (float): Distancia máxima para que una antena sea backup.
    b (int): Cantidad máxima de conjuntos de backup a los que puede pertenecer una antena.
    k (int): Tamaño del conjunto de backup requerido para cada antena.
    """

    G = nx.DiGraph()

    # Definimos nombres para la fuente y el sumidero
    fuente = 'fuente'
    sumidero = 'sumidero'

    # Construimos el Grafo
    for i in range(1, n + 1):
        # Nodo de necesidad (antena i necesita backup)
        nodo_A = f"A_{i}"
        # Nodo proveedor (antena i ofrece backup)
        nodo_B = f"B_{i}"

        # Conexión desde la fuente a los nodos A con capacidad k
        G.add_edge(fuente, nodo_A, capacity=k)
        # Conexión desde los nodos B al sumidero con capacidad b
        G.add_edge(nodo_B, sumidero, capacity=b)

    # Conexiones entre A y B basadas en la distancia
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:  # Una antena no suele ser backup de sí misma
                # Ajustamos índices para la matriz d (que es 0-indexed en Python)
                distancia = d[i-1][j-1]
                if distancia < D:
                    G.add_edge(f"A_{i}", f"B_{j}", capacity=1)

    # 2. Ejecución de Edmonds-Karp
    # nx.maximum_flow utiliza Edmonds-Karp por defecto si se especifica la función.
    valor_flujo, flujo_dict = nx.maximum_flow(G, fuente, sumidero, flow_func=nx.algorithms.flow.edmonds_karp)

    # 3. Verificación de la solución
    flujo_esperado = n * k
    if valor_flujo < flujo_esperado:
        return None  # No existe una solución posible que cumpla las restricciones

    # 4. Reconstrucción de la solución
    resultado_backups = {}
    for i in range(1, n + 1):
        nodo_A = f"A_{i}"
        resultado_backups[i] = []

        # Revisamos a qué nodos B se les envió flujo desde A_i
        for nodo_B, flujo_enviado in flujo_dict[nodo_A].items():
            if flujo_enviado == 1:
                # Extraemos el número de la antena proveedora
                id_proveedora = int(nodo_B.split("_")[1])
                resultado_backups[i].append(id_proveedora)

    return resultado_backups


if __name__ == "__main__":
    n = 3
    D = 5  # Distancia máxima de cobertura
    b = 1  # Máximo de veces que una antena puede ser backup
    k = 1

    # Matriz de distancias de ejemplo (4x4)
    matriz_distancias = [
        [0,  3,  4],
        [3,  0,  4],
        [4,  4,  0],
    ]

    solucion = buscar_conjuntos_backup(n, matriz_distancias, D, b, k)
    print(solucion)

    if solucion:
        print("¡Solución encontrada exitosamente!")
        for antena, backups in solucion.items():
            print(f"Antena {antena} -> Conjunto de backup: {backups}")
    else:
        print("No existe una solución posible con las restricciones dadas.")