import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint


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
    print("Podaj k:")
    k = int(input())
    print("Podaj T:")
    T = int(input())
    t = np.linspace(0, 10, 50)
    _, ax = plt.subplots(figsize=(10, 10))
    ax.plot(t, k / T * np.exp(-t / T), label='Odpowiedz impulsowa')
    ax.plot(t, k * (1 - np.exp(-t / T)), label='Odpowiedz skokowa')
    ax.legend()
    plt.show()


def task3():
    print("Podaj k:")
    k = int(input())
    print("Podaj T:")
    T = int(input())
    t = np.linspace(0, 10, 50)
    _, ax = plt.subplots(figsize=(10, 10))
    ax.plot(t, k * (1 - np.exp(-t / T)), label='Odpowiedz impulsowa')
    ax.plot(t, (t - T * (1 - np.exp(-t / T))) / k, label='Odpowiedz skokowa')
    ax.legend()
    plt.show()


def task4():
    t_12 = 5730
    k = np.log(2) / t_12
    n_0 = 1000

    t = np.linspace(0, 5730 * 2, n_0)
    _, ax = plt.subplots(figsize=(10, 10))

    ax.plot(t, n_0 * np.exp(-k * t), label='Rozpad promieniotwórczy')

    ax.set_xlabel('t')
    ax.set_ylabel('N')
    ax.set_title("Wykres")
    ax.legend()
    plt.show()


def task5():
    t = np.linspace(0, 100, 1000)
    x_init = [0, 0]
    b = int(input("Podaj stałą tłumienia: "))
    k = int(input("Podaj sztywność sprężyny: "))
    m = int(input("Podaj masę układu: "))
    F = int(input("Podaj wartość siły działającej na układ: "))

    x = odeint(mydiff, x_init, t, args=(F, b, k, m))
    x1 = x[:, 0]
    x2 = x[:, 1]

    plt.plot(t, x1)
    plt.plot(t, x2)
    plt.title('Układ o masie m ze sprężyną i tłumieniem')
    plt.xlabel('t')
    plt.ylabel('x(t)')
    plt.legend(["Położenie", "Szybkość układu"])
    plt.grid()
    plt.show()


def mydiff(x, t, F, b, k, m):
    dx1dt = x[1]
    dx2dt = (F - b * x[1] - k * x[0]) / m
    dxdt = [dx1dt, dx2dt]

    return dxdt


def lab2():
    task1()
    task2()
    task3()
    task4()
    task5()


if __name__ == "__main__":
    lab2()
