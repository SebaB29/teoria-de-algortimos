# Trabajo Práctico 2 - Problema 1

## Requisitos

- Python 3.10 o superior
- Recomendado: `pulp` o el solver que utilice para los `.lp`

## Estructura

- `problema_1.py`: implementación principal que procesa archivos de `test_data`.
- `run_test_data.sh`: script para ejecutar todos los `test_data` y volcar resultados en `results.txt`.
- `model/`: contiene modelos en formato `.lp` (ej.: `modelo_ofertas_10.lp`).
- `test_data/`: archivos CSV con instancias de prueba.
- `results.txt`: salida agregada de ejecuciones por lote.

## Formato de `test_data` (CSV)

Cada fila representa una oferta con columnas separadas por comas. Ejemplo de línea:

```
A,1,50000,30
```

Se interpreta como: `identificador, cantidad, precio, tiempo` (o columnas análogas según el enunciado del TP). Ajustar el parser en `problema_1.py` si su formato real difiere.

## Ejecución

Ejecutar un caso puntual:

```bash
python3 problema_1.py test_data/ofertas_10.csv
```

Ejecutar todos los casos (usa `run_test_data.sh`):

```bash
chmod +x run_test_data.sh
./run_test_data.sh
```

Los resultados por lote se almacenan en `results.txt`.

## Modelos

Los archivos en `model/` son formulaciones en `.lp` que pueden probarse con un solver de programación lineal/entera.
