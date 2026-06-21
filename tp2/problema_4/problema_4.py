import random


def colorear_3_colores(Grafo):
    colores = {}
    for vertice in Grafo:
        colores[vertice] = random.randint(0,  2)

    return colores


def calcular_aristas_satisfechas(Grafo):
    vertices_coloreados = colorear_3_colores(Grafo)
    contador_vertices = 0
    aristas_visitadas = []

    for u in Grafo:
        for v in Grafo[u]:
            if (v, u) not in aristas_visitadas:
                aristas_visitadas.append((u, v))
                if (vertices_coloreados[u] != vertices_coloreados[v]):
                    contador_vertices += 1

    return contador_vertices
