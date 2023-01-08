import matplotlib.pyplot as plt

PATH = "/home/blairi/development/projects/sorting-algorithms"


def get_data(path:str) -> tuple[list[int], list[int]]:

    file = open(path, "r")

    ns = list()
    times = list()
    for line in file:

        line = line.rstrip()
        if line == "":
            continue

        n = line.split(":")[0]
        time = line.split(":")[1]

        ns.append( int(n) )
        times.append( int(time) )

    file.close()

    return ( ns, times )


def menu() -> None:
    title = str
    n_best, steps_best = (int, int)
    n_worst, steps_worst = (int, int)
    n_average, steps_average = (int, int)

    while True:
        print("Choose a sorting algorithm from the list typing the number")
        print("0. Exit")
        print("1. Bubble sort")
        print("2. Merge sort")
        print("3. Heap sort")
        opc = input(": ")
        if not opc.isdigit():
            print("Illegal choice.")
            continue
        
        opc = int(opc)

        if opc == 0: # Exit
            break

        if opc == 1: # Bubble sort
            title = "Bubble sort"
            n_best, steps_best = get_data(f"{PATH}/bubblesort/data/best_case.txt")
            n_worst, steps_worst = get_data(f"{PATH}/bubblesort/data/worst_case.txt")
            n_average, steps_average = get_data(f"{PATH}/bubblesort/data/average_case.txt")
        
        if opc == 2: # Merge sort
            title = "Merge sort"
            n_best, steps_best = get_data(f"{PATH}/mergesort/data/best_case.txt")
            n_worst, steps_worst = get_data(f"{PATH}/mergesort/data/worst_case.txt")
            n_average, steps_average = get_data(f"{PATH}/mergesort/data/average_case.txt")
        
        if opc == 3:
            title = "Heap sort"
            n_best, steps_best = get_data(f"{PATH}/heapsort/data/best_case.txt")
            n_worst, steps_worst = get_data(f"{PATH}/heapsort/data/worst_case.txt")
            n_average, steps_average = get_data(f"{PATH}/heapsort/data/average_case.txt")
        
        # Graph building...
        fig, (ax0, ax1, ax2) = plt.subplots(nrows=1, ncols=3, figsize=(12, 6))
        plt.suptitle(title, fontsize=16)

        ax0.set_title("Worst case")
        ax0.set_xlabel("Elements (n)")
        ax0.set_ylabel("Number of steps")
        ax0.plot(n_worst, steps_worst, marker = "*", color = "r")

        ax1.set_title("Best case")
        ax1.set_xlabel("Elements (n)")
        ax1.set_ylabel("Number of steps")
        ax1.plot(n_best, steps_best, marker = "*", color = "g")

        ax2.set_title("Average case")
        ax2.set_xlabel("Elements (n)")
        ax2.set_ylabel("Number of steps")
        ax2.plot(n_average, steps_average, marker = "*", color = "b")

        plt.show()


def main() -> None:
    menu()


main()