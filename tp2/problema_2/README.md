# Trabajo Práctico 2 - Problema 2

## Requisitos

- Python 3.10 o superior
- Bibliotecas: `networkx`

## Estructura

- `problema_2.py`: contiene la función `buscar_conjuntos_backup(...)` que construye un grafo dirigido y usa Edmonds-Karp para calcular flujos máximos.
- `RedesDeFlujo.ipynb`: notebook con experimentos y visualizaciones sobre flujos y cobertura.

## Descripción

El enfoque modela antenas como nodos con demanda y oferta de backup, construyendo una fuente y un sumidero y usando un algoritmo de flujo (Edmonds-Karp) para verificar factibilidad y reconstruir conjuntos de backup.

## Ejecución

Ejecutar el ejemplo incluido:

```bash
python3 problema_2.py
```

## Mediciones

En el notebook `RedesDeFlujo.ipynb` se agrego un generador de instancias aleatorias para medir el tiempo de ejecución del algoritmo en función del número de antenas y la densidad de backup. Se incluyen gráficos que muestran el comportamiento empírico del tiempo de ejecución.