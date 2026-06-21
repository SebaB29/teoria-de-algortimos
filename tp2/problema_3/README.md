# Trabajo Práctico 2 - Problema 3

## Requisitos

- Python 3.10 o superior

## Estructura

- `problema_3.py`: implementación del algoritmo de aproximación (greedy ordenado) y script de ejecución.
- `generar_test_data.py`: generador de instancias de prueba.
- `run_test_data.sh`: ejecuta todos los casos en `test_data` y vuelca los resultados en `results.txt`.
- `mediciones_p3.ipynb`: notebook de mediciones y visualizaciones.

## Formato de `test_data/*.txt`

Cada archivo debe respetar este formato:

1. Primera línea: valor entero `B` (capacidad/cota).
2. Segunda línea: lista de enteros (elementos del conjunto `A`) separados por espacios o comas.

Ejemplo:

```
50
20,15,10,5
```

## Ejecución

Ejecutar un caso puntual:

```bash
python3 problema_3.py test_data/100.txt
```

Ejecutar todos los casos:

```bash
chmod +x run_test_data.sh
./run_test_data.sh
```

La salida por lote se guarda en `results.txt`.

## Notebook de mediciones

`mediciones_p3.ipynb` contiene generación de instancias, mediciones de tiempo y gráficos de comportamiento empírico.
