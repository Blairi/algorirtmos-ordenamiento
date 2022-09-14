import random
from Animal import Animal
from generarCadena import generarCadena

def countingSort(A, k):

    C = [ 0 for _ in range(k + 1) ]
    B = [ 0 for _ in range(len(A)) ]

    for j in range(0, len(A)):
        C[A[j]] = C[A[j]] + 1

    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]
    
    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] = C[A[j]] - 1

    return B


# Animal(random.randint(0, 100), generarCadena(20))
A = []
for _ in range(10):
    A.append( random.randint(0, 100) )

for animal in A:
    print(animal)

print(A)
print(countingSort(A, max(A)))

print(int("hola"))