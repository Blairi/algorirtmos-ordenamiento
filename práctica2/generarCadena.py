import random
import string

def generarCadena(longitud) -> str:
    cad = ""
    alfabeto = list(string.ascii_lowercase)
    for _ in range(longitud):
        cad += alfabeto[random.randint(0, len(alfabeto) - 1)]
    return cad

