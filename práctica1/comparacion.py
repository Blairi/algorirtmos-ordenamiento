import random
import matplotlib.pyplot as plt

def crearSubArreglo(A, indIzq, indDer):
    return A[indIzq:indDer + 1]

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



def timesBubbleSort( A ):
    times = 0
    for i in range( 1, len( A ) + 1 ):
        times += 1
        for j in range( len(A) - 1 ):
            times += 1
            if A[j] > A[j + 1]:
                temp = A[j]
                A[j] = A[j + 1]
                A[j + 1] = temp

    return times

A = []
A_times = []
A_elementos = []
for i in range(100):
    A.append( random.randint(1, 100) )
    A_times.append( timesBubbleSort(A) )
    A_elementos.append( len(A) )

B = []
B_times = []
B_elementos = []
for i in range(100):
    B.append( random.randint(1, 100) )
    B_times.append( timesMergeSort(B, 0, len(B) - 1) )
    B_elementos.append( len(B) )


# Construyendo gráfica...
fig, ax = plt.subplots()

ax.plot(A_times, A_elementos, label = 'Bubble sort', marker = '*', color = 'b')
ax.plot(B_times, B_elementos, label = 'Merge sort', marker = 'o', color = 'r')

plt.title('Merge sort VS Bubble sort')
ax.set_xlabel('Veces que entra')
ax.set_ylabel('Elementos')
ax.grid(True)
ax.legend(loc=2)

plt.show()
