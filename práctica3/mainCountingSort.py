import random
from countingSort import timesCountingSort
import matplotlib.pyplot as plt
from Animal import Animal
from generarCadena import generarCadena

MAX = 1000
def func (p): # función "key" para obtener edad máxima con max()
    return p.edad

#Caso promedio
A = []
A_times = []
A_elementos = []
for i in range(MAX):
    A.append( Animal(random.randint(0, 1000), generarCadena(10)) )
    listaOrdenada, times = timesCountingSort(A, Animal.getEdad, max(A, key=func))
    A_times.append( times )
    A_elementos.append(len(A))

#Mejor caso
B = []
B_times = []
B_elementos = []
for i in range(MAX):
    B.append( Animal(i, generarCadena(10)) )
    listaOrdenada, times = timesCountingSort(B, Animal.getEdad, max(A, key=func))
    B_times.append( times )
    B_elementos.append(len(B))

# Caso peor
C = []
C_times = []
C_elementos = []
for i in range(MAX, 0, -1):
    C.append( Animal(i, generarCadena(10)) )
    listaOrdenada, times = timesCountingSort(C, Animal.getEdad, max(A, key=func))
    C_times.append( times )
    C_elementos.append(len(C))

# Construyendo gráfica...
fig, ax = plt.subplots()
ax.plot(A_times, A_elementos, label = 'Caso promedio', marker = '*', color = 'b')
ax.plot(B_times, B_elementos, label = 'Mejor caso', marker = 'o', color = 'g')
ax.plot(C_times, C_elementos, label = 'Peor caso', marker = 'x', color = 'r')

plt.title('Counting sort')
ax.set_xlabel('Veces que entra')
ax.set_ylabel('Elementos')
ax.grid(True)
ax.legend(loc=2)

plt.show()
