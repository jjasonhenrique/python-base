#!/usr/bin/env python3
"""
Imprime a tabuada de 1 a 10
"""

__version__ = "0.1.0"
__author__  = "Jason"

base = list(range(1,11))

for numero in base:
    print("A tabuada do numero", numero, ":")
    for outro_numero in base:
        resultado = numero * outro_numero
        print(numero, "X", outro_numero, "=", resultado) 
    print("-----------------------------")
