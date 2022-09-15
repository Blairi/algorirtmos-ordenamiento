import random
from Animal import Animal
from generarCadena import generarCadena

def countingSort(A, attr, k):

    C = [ 0 for _ in range(attr(k) + 1) ]
    B = [ 0 for _ in range(len(A)) ]

    for j in range(0, len(A)):
        C[attr(A[j])] = C[attr(A[j])] + 1

    for i in range(1, attr(k) + 1):
        C[i] = C[i] + C[i - 1]
    
    for j in range(len(A) - 1, -1, -1):
        B[C[attr(A[j])] - 1] = A[j]
        C[attr(A[j])] = C[attr(A[j])] - 1

    return B

def timesCountingSort(A, attr, k):
    times = 0

    C = [ 0 for _ in range(attr(k) + 1) ]
    B = [ 0 for _ in range(len(A)) ]

    for j in range(0, len(A)):
        times += 1

        C[attr(A[j])] = C[attr(A[j])] + 1

    for i in range(1, attr(k) + 1):
        times += 1

        C[i] = C[i] + C[i - 1]
    
    for j in range(len(A) - 1, -1, -1):
        times += 1

        B[C[attr(A[j])] - 1] = A[j]
        C[attr(A[j])] = C[attr(A[j])] - 1

    return B, times


# Animal(random.randint(0, 100), generarCadena(20))
# A = []
# for _ in range(10):
#     A.append( Animal(random.randint(0, 100), generarCadena(20)) )

# for animal in A:
#     print(animal)

# print('\n')

# listaCopia = A.copy()

# quick_sort(listaCopia, Animal.getEdad, 0, len(A) - 1)


# A_ordenada = countingSort(A, Animal.getEdad, listaCopia[len(listaCopia) - 1])
# for animalOrdenado in A_ordenada:
#     print(animalOrdenado)


# Animal(random.randint(0, 100), generarCadena(20))
# A = []
# for _ in range(10):
#     A.append( Animal(random.randint(0, 100), generarCadena(20)) )

# for animal in A:
#     print(animal)

# print('\n')

# def func (p):
#     return p.edad

# A_ordenada = countingSort(A, Animal.getEdad, max(A, key=func))
# for animalOrdenado in A_ordenada:
#     print(animalOrdenado)