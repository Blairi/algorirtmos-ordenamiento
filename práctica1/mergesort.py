import random
import matplotlib.pyplot as plt

# Prueba de funcionamiento
def crearSubArreglo(A, indIzq, indDer):
    return A[indIzq:indDer + 1]


def merge(A, p, q, r):
    izq = crearSubArreglo( A, p, q )
    der = crearSubArreglo( A, q + 1, r )

    i = 0
    j = 0
    for k in range( p, r + 1 ):
        if ( j >= len( der ) ) or ( i < len( izq ) and izq[i] < der[j] ):
            A[k] = izq[i]
            i = i + 1
        else:
            A[k] = der[j]
            j = j + 1


def mergeSort(A, p, r):
    if r - p > 0:
        q = int( (p + r) / 2 )
        mergeSort( A, p, q )
        mergeSort( A, q + 1, r )
        merge( A, p, q, r )
        return A


prueba = []
for i in range(20):
    prueba.append(random.randint(1, 20))

print(prueba)
print(mergeSort(prueba, 0, len(prueba) - 1))


# Modificando funciones para contar
def timesMerge(A, p, q, r):

    times = 0

    izq = crearSubArreglo( A, p, q )
    der = crearSubArreglo( A, q + 1, r )

    i = 0
    j = 0
    for k in range( p, r + 1 ):
        times += 1
        if ( j >= len( der ) ) or ( i < len( izq ) and izq[i] < der[j] ):
            A[k] = izq[i]
            i = i + 1
        else:
            A[k] = der[j]
            j = j + 1

    return times


def timesMergeSort(A, p, r):
    times = 0
    if r - p > 0:
        q = int( (p + r) / 2 )
        times += timesMergeSort( A, p, q )
        times += timesMergeSort( A, q + 1, r )
        times += timesMerge( A, p, q, r )
    return times


# Caso promedio
A = []
A_times = []
A_elementos = []
for i in range(100):
    A.append( random.randint(1, 100) )
    A_times.append( timesMergeSort(A, 0, len(A) - 1) )
    A_elementos.append( len(A) )

# Mejor caso
B = []
B_times = []
B_elementos = []
for i in range( 100 ):
    B.append(i)
    B_times.append( timesMergeSort(B, 0, len(B) - 1) )
    B_elementos.append( len(B) )


# Peor caso
C = []
C_times = []
C_elementos = []
for i in range( 100, 0, -1 ):
    C.append(i)
    C_times.append( timesMergeSort(C, 0, len(C) - 1) )
    C_elementos.append( len(C) )

# Construyendo gráfica...
fig, ax = plt.subplots()

ax.plot(A_times, A_elementos, label = 'Caso promedio', marker = '*', color = 'b')
ax.plot(B_times, B_elementos, label = 'Mejor caso', marker = 'o', color = 'g')
ax.plot(C_times, C_elementos, label = 'Peor caso', marker = 'x', color = 'r')

plt.title('Merge sort')
ax.set_xlabel('Veces que entra')
ax.set_ylabel('Elementos')
ax.grid(True)
ax.legend(loc=2)

plt.show()

