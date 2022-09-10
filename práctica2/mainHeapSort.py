from string import ascii_lowercase
import random
from generarCadena import generarCadena
from Car import Car
import matplotlib.pyplot as plt
from heapSort import heapSort, timesHeapSort

"""

 Prueba

"""
prueba = []
for _ in range(10):
    prueba.append(Car(random.randint(99, 99999), generarCadena(20)))

print("Lista inicial:")
for car in prueba:
    print(car)

heapSort(prueba, Car.getModel, len(prueba))

print("Lista ordenada:")
for car in prueba:
    print(car)

"""

 Generación de gráficas

"""


MAX = 100


# Caso promedio
A = []
A_times = []
A_elementos = []
for i in range(MAX):
    A.append( Car(random.randint(0, 9999999), generarCadena(10)) )
    A_times.append( timesHeapSort(A, Car.getModel , len(A)) )
    A_elementos.append( len(A) )
# for car in A:
    # print(car)


# Mejor caso
alfabeto = list(ascii_lowercase)
B = []
B_times = []
B_elementos = []
modelo = ""
for i in range(MAX):
    modelo += alfabeto[i if i < len(alfabeto) else random.randint(0, len(alfabeto) - 1) ]
    B.append(Car(i * 2, modelo))
    B_times.append( timesHeapSort(B, Car.getModel, len(B)) )
    B_elementos.append( len(B) )
# for car in B:
    # print(car)


# Peor caso
C = []
C_times = []
C_elementos = []
modelo = ""
for i in range(MAX, 0, -1):
    modelo += alfabeto[-i if -i > -len(alfabeto) else random.randint(-len(alfabeto) + 1, 0)]
    C.append(Car(i * 2, modelo))
    C_times.append( timesHeapSort(C, Car.getModel, len(C)) )
    C_elementos.append( len(C) )
# for car in C:
    # print(car)

# Construyendo gráfica...
fig, ax = plt.subplots()
ax.plot(A_times, A_elementos, label = 'Caso promedio', marker = '*', color = 'b')
ax.plot(B_times, B_elementos, label = 'Mejor caso', marker = 'o', color = 'g')
ax.plot(C_times, C_elementos, label = 'Peor caso', marker = 'x', color = 'r')

plt.title('Heap sort')
ax.set_xlabel('Veces que entra')
ax.set_ylabel('Elementos')
ax.grid(True)
ax.legend(loc=2)

plt.show()
