#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente

Como usar:
Tenha a variavel LANG devidamente configurada exemplo:

    export LANG=en_US.UTF-8

Execução:
    ./hello.py ou python3 hello.py
"""
__version__ = "0.0.1"
__author__  = "Jason Henrique"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]
msg = "Hello World"

if current_language == "pt_BR":
    msg = "Ola Mundo"
    

print(msg)


