import matplotlib.pyplot as plt

PATH = "/home/blairi/development/projects/sorting-algorithms/bubblesort/data/"


def get_data(path:str) -> tuple[list[int], list[float]]:

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
        times.append( float(time) )

    file.close()

    return ( ns, times )


def main() -> None:

    n_best, steps_best = get_data(f"{PATH}best_case.txt")
    n_worst, steps_worst = get_data(f"{PATH}worst_case.txt")
    n_average, steps_average = get_data(f"{PATH}average_case.txt")

    fig, (ax0, ax1, ax2) = plt.subplots(nrows=1, ncols=3, figsize=(12, 6))

    ax0.set_title("Worst case")
    ax0.plot(n_worst, steps_worst, marker = "*", color = "r")

    ax1.set_title("Best case")
    ax1.plot(n_best, steps_best, marker = "*", color = "g")

    ax2.set_title("Average case")
    ax2.plot(n_average, steps_average, marker = "*", color = "b")

    plt.show()


main()