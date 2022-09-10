from string import ascii_lowercase
import random
from generarCadena import generarCadena
from quickSort import quick_sort, timesQuick_sort
from Car import Car
import matplotlib.pyplot as plt

"""

 Prueba

"""
prueba = []
for _ in range(10):
    prueba.append(Car(random.randint(99, 99999), generarCadena(20)))

print("Lista inicial:")
for car in prueba:
    print(car)

quick_sort(prueba, Car.getModel, 0, len(prueba) - 1)

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
    A_times.append( timesQuick_sort(A, Car.getModel , 0, len(A) - 1) )
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
    B_times.append( timesQuick_sort(B, Car.getModel, 0, len(B) - 1) )
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
    C_times.append( timesQuick_sort(C, Car.getModel, 0, len(C) - 1) )
    C_elementos.append( len(C) )
# for car in C:
    # print(car)


# Construyendo gráfica...
fig, ax = plt.subplots()
ax.plot(A_times, A_elementos, label = 'Caso promedio', marker = '*', color = 'b')
ax.plot(B_times, B_elementos, label = 'Mejor caso', marker = 'o', color = 'g')
ax.plot(C_times, C_elementos, label = 'Peor caso', marker = 'x', color = 'r')
plt.title('Quick sort')
ax.set_xlabel('Veces que entra')
ax.set_ylabel('Elementos')
ax.grid(True)
ax.legend(loc=2)
plt.show()
