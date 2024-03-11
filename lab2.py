import networkx as nx
import numpy as np
from matplotlib import pyplot as plt


def task1():
    r = int(input("Podaj rozstaw osi robota: "))
    u_p = int(input("Podaj prędkość liniową prawego koła: "))
    u_l = int(input("Podaj prędkość liniową lewego koła: "))

    t = np.linspace(0, 10, 50)
    _, ax = plt.subplots(figsize=(10, 5))

    ax.plot(t, t / r * (u_p - u_l), label='Prędkość kątowa obrotu robota')

    ax.set_xlabel('t')
    ax.set_ylabel('w')
    ax.set_title("Wykres")
    ax.legend()
    plt.show()


def task2():
    pass


def task3():
    pass


def task4():
    pass


def task5():
    pass


def lab2():
    task1()
    task2()
    task3()
    task4()
    task5()


if __name__ == "__main__":
    lab2()
