#!/usr/bin/env python3
"""
Imprime a tabuada de 1 a 10
"""

__version__ = "0.1.1"
__author__  = "Jason"

base = list(range(1,11))

for n1 in base:
    print("{:-^170}".format(f"Tabuada do numero {n1}:")+ "\n")
    for n2 in base:
        resultado = n1 * n2
        print("{:^170}".format(f"{n1} X {n2} = {resultado}"))
    print("#" * 170 + "\n")