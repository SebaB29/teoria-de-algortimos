#!/bin/bash

test_data="test_data"
output="results.txt"

> "$output"

ls -v "$test_data"/*.txt | while read archivo; do

    python3 problema_3.py "$archivo" >> "$output"
    echo "" >> "$output"
done

echo "Todos los resultados se han guardado en '$output'."
