# Trabajo Practico 2 - TDA (2026 1C)

## Requisitos generales

- Python 3.10 o superior
- Bibliotecas: `numpy`, `networkx`, `matplotlib`

## Estructura de la carpeta

- `problema_1/`: modelo (LP), datos de prueba `test_data`, script de ejecución y resultados.
- `problema_2/`: implementación basada en flujos y notebook de apoyo `RedesDeFlujo.ipynb`.
- `problema_3/`: implementación del algoritmo, generador de casos y mediciones.
- `problema_4/`: implementación, script para generar métricas y gráficas.
- `util.py`: utilidades compartidas.

Cada carpeta de `problema_*` contiene su propio `README.md` con formato de entrada, ejecución y resultados.

## Ejecución rápida por problema

### Problema 1

```bash
cd problema_1
bash run_test_data.sh
```

### Problema 2

```bash
cd problema_2
python3 problema_2.py
```

### Problema 3

```bash
cd problema_3
chmod +x run_test_data.sh
./run_test_data.sh
```

### Problema 4

```bash
cd problema_4
python3 generar_metricas.py
```

## Notebooks y mediciones

- `problema_3/mediciones_p3.ipynb` y `problema_2/RedesDeFlujo.ipynb` contienen experimentos y visualizaciones.

## Regeneración de sets de datos

Los problemas que incluyen generadores tienen scripts nombrados `generar_*` (ej.: `generar_test_data.py`, `generar_metricas.py`).

Ejemplo:

```bash
cd problema_3
python3 generar_test_data.py
```