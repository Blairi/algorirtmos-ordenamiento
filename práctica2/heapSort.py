def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp

def hIzq(i):
    return 2 * i + 1

def hDer(i):
    return 2 * i + 2

def maxHeapify(A, attr, i, tamanoHeap):
    L = hIzq(i)
    R = hDer(i)
    if L <= tamanoHeap - 1 and attr(A[L]) > attr(A[i]):
        posMax = L
    else:
        posMax = i
    if R <= tamanoHeap - 1 and attr(A[R]) > attr(A[posMax]):
        posMax = R
    if posMax != i:
        swap(A, i, posMax)
        maxHeapify(A, attr, posMax, tamanoHeap)

def construirHeapMaxIni(A, attr, tamanoHeap):
    for i in range(tamanoHeap // 2, -1, -1):
        maxHeapify(A, attr, i, tamanoHeap)

def heapSort(A, attr, tamanoHeap):
    construirHeapMaxIni(A, attr, tamanoHeap)
    for i in range(len(A) - 1, 0, -1):
        swap(A, 0, i)
        tamanoHeap = tamanoHeap - 1
        maxHeapify(A, attr, 0, tamanoHeap)



# A = []
# for _ in range(100):
#     A.append(Car(random.randint(0, 9999999), generarCadena(10)))

# heapSort(A, Car.getId, len(A))
# for car in A:
#     print(car)

def timesMaxHeapify(A, attr, i, tamanoHeap):
    times = 0
    L = hIzq(i)
    R = hDer(i)
    if L <= tamanoHeap - 1 and attr(A[L]) > attr(A[i]):
        posMax = L
    else:
        posMax = i
    if R <= tamanoHeap - 1 and attr(A[R]) > attr(A[posMax]):
        posMax = R
    if posMax != i:
        swap(A, i, posMax)
        times += timesMaxHeapify(A, attr, posMax, tamanoHeap)
    times += 1
    return times

def timesConstruirHeapMaxIni(A, attr, tamanoHeap):
    times = 0
    for i in range(tamanoHeap // 2, -1, -1):
        times += 1
        times += timesMaxHeapify(A, attr, i, tamanoHeap)
    return times

def timesHeapSort(A, attr, tamanoHeap):
    times = 0
    times += timesConstruirHeapMaxIni(A, attr, tamanoHeap)
    for i in range(len(A) - 1, 0, -1):
        swap(A, 0, i)
        tamanoHeap = tamanoHeap - 1
        times += 1
        times += timesMaxHeapify(A, attr, 0, tamanoHeap)
    return times