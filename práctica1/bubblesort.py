import random
import matplotlib.pyplot as plt

# Prueba de funcionamiento
def bubbleSort( A ):
    for i in range( 1, len( A ) + 1 ):
        for j in range( len(A) - 1 ):
            if A[j] > A[j + 1]:
                temp = A[j]
                A[j] = A[j + 1]
                A[j + 1] = temp
    return A

prueba = []
for i in range( 20 ): # Generamos lista de 20 elementos
    prueba.append( random.randint(1, 100) )

print( prueba )
print(bubbleSort( prueba ))

"""
 Generación de gráficas
"""

# Función para contar
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


# Caso promedio
A = []
A_times = [] # lista para guardar el número de veces que entra a los ciclos correspondiente a los elementos en A
A_elementos = [] # lista para guardar la cantidad de elementos
for i in range( 100 ):
    A.append( random.randint(0, 20) )
    A_times.append( timesBubbleSort(A) )
    A_elementos.append( len(A) )


# Mejor caso
B = []
B_times = []
B_elementos = []
for i in range( 100 ):
    B.append(i)
    B_times.append( timesBubbleSort(B) )
    B_elementos.append( len(B) )


# Peor caso
C = []
C_times = []
C_elementos = []
for i in range( 100, 0, -1 ):
    C.append(i)
    C_times.append( timesBubbleSort(C) )
    C_elementos.append( len(C) )


# Construyendo gráfica...
fig, ax = plt.subplots()

ax.plot(A_times, A_elementos, label = 'Caso promedio', marker = '*', color = 'b')
ax.plot(B_times, B_elementos, label = 'Mejor caso', marker = 'o', color = 'g')
ax.plot(C_times, C_elementos, label = 'Peor caso', marker = 'x', color = 'r')

plt.title('Bubble Sort')
ax.set_xlabel('Veces que entra')
ax.set_ylabel('Elementos')
ax.grid(True)
ax.legend(loc=2)

plt.show()
