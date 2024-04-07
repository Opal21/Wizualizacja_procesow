import numpy as np
import matplotlib.pyplot as plt


def task1():
    """
    Wykorzystaj jawną metodę Eulera do numerycznego uzyskania odpowiedzi członu inercyjnego na pobudzenia
     • skokowe,
     • impulsowe (przybliżona delta Diraca).
    Wyświetl przebiegi w czasie dla kilku kroków dyskretyzacji.
    Porównaj z odpowiedzią wyznaczoną analitycznie (z poprzedniej listy/z wykładu).
    """
    pass


def task2():
    """
    Numerycznie (metoda Eulera) wyznacz odpowiedzi członów
    • inercyjnego drugiego rzędu,
    • całkującego z inercją,
    na pobudzenie
    • sinusoidalne,
    • impulsowe (okresowe).
    dla zadanego kroku dyskretyzacji.
    """
    pass


def task3():
    # Parametry symulacji
    initial_state = np.array([0.0, 0.0, 0.0])  # Początkowy stan [x_1, x_2, x_3]
    duration = float(input("Podaj czas trwania symulacji: "))
    dt = float(input("Podaj krok czasowy (dt): "))

    # Symulacja ruchu prostoliniowego
    linear_trajectory = simulate_motion(initial_state, linear_motion_control, duration, dt)

    # Symulacja ruchu po okręgu
    circular_trajectory = simulate_motion(initial_state, circular_motion_control, duration, dt)

    # Symulacja naprzemiennego ruchu prostoliniowego i po okręgu
    alternating_trajectory = simulate_motion(initial_state, alternating_motion_control, duration, dt)

    # Wykres
    plt.figure(figsize=(10, 6))
    plt.plot(linear_trajectory[:, 0], linear_trajectory[:, 1], label='Ruch prostoliniowy')
    plt.plot(circular_trajectory[:, 0], circular_trajectory[:, 1], label='Ruch po okręgu')
    plt.plot(alternating_trajectory[:, 0], alternating_trajectory[:, 1], label='Naprzemienny ruch')
    plt.scatter(initial_state[0], initial_state[1], color='red', label='Początkowa pozycja', zorder=5)
    plt.xlabel('x_1')
    plt.ylabel('x_2')
    plt.title('Trajektoria ruchu dwukołowego robota mobilnego')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()


def task4():
    # Wczytanie danych od użytkownika
    H = int(input("Podaj horyzont czasowy H (w dniach): "))
    r = float(input("Podaj parametr r (zysk na koncie): "))
    h = float(input("Podaj koszt składowania pszenicy (w tonach): "))
    x0 = float(input("Podaj początkowe saldo konta (x0): "))
    y0 = float(input("Podaj początkową ilość składowanej pszenicy (y0): "))

    # Wczytanie ciągu wartości funkcji v(t) i p(t)
    v = []
    p = []
    for _ in range(H):
        v_t = float(input("Podaj prędkość skupu pszenicy na dzień {}: ".format(_ + 1)))
        p_t = float(input("Podaj cenę tony pszenicy na dzień {}: ".format(_ + 1)))
        v.append(v_t)
        p.append(p_t)

    # Wywołanie metody Eulera
    x, y = euler_method(r, h, x0, y0, v, p)

    # Wyświetlenie wyników
    plt.figure(figsize=(10, 6))

    plt.plot(range(H + 1), x, label="Saldo konta (x(t))")

    plt.plot(range(H + 1), y, label="Składowana pszenica (y(t))")

    plt.legend()
    plt.tight_layout()
    plt.grid(True)
    plt.show()


def task5():
    # Parametry symulacji
    initial_state = np.array([0.0, 0.0, 0.0])  # Początkowy stan [x_1, x_2, x_3]
    duration = float(input("Podaj czas trwania symulacji: "))
    dt = float(input("Podaj krok czasowy (dt): "))

    # Symulacja ruchu prostoliniowego z użyciem RK-2
    linear_trajectory_rk2 = simulate_motion(initial_state, linear_motion_control, duration, dt, rk2_integration)

    # Symulacja ruchu po okręgu z użyciem RK-2
    circular_trajectory_rk2 = simulate_motion(initial_state, circular_motion_control, duration, dt, rk2_integration)

    # Symulacja naprzemiennego ruchu prostoliniowego i po okręgu z użyciem RK-2
    alternating_trajectory_rk2 = simulate_motion(initial_state, alternating_motion_control, duration, dt,
                                                 rk2_integration)

    # Symulacja ruchu prostoliniowego z użyciem RK-4
    linear_trajectory_rk4 = simulate_motion(initial_state, linear_motion_control, duration, dt, rk4_integration)

    # Symulacja ruchu po okręgu z użyciem RK-4
    circular_trajectory_rk4 = simulate_motion(initial_state, circular_motion_control, duration, dt, rk4_integration)

    # Symulacja naprzemiennego ruchu prostoliniowego i po okręgu z użyciem RK-4
    alternating_trajectory_rk4 = simulate_motion(initial_state, alternating_motion_control, duration, dt,
                                                 rk4_integration)
    # Wykres
    plt.figure(figsize=(14, 10))

    # Trajektoria ruchu z użyciem RK-2
    plt.subplot(2, 1, 1)
    plt.plot(linear_trajectory_rk2[:, 0], linear_trajectory_rk2[:, 1], label='Ruch prostoliniowy')
    plt.plot(circular_trajectory_rk2[:, 0], circular_trajectory_rk2[:, 1], label='Ruch po okręgu')
    plt.plot(alternating_trajectory_rk2[:, 0], alternating_trajectory_rk2[:, 1], label='Naprzemienny ruch')
    plt.scatter(initial_state[0], initial_state[1], color='red', label='Początkowa pozycja', zorder=5)
    plt.xlabel('x_1')
    plt.ylabel('x_2')
    plt.title('Ruch prostoliniowy z użyciem RK-2')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')

    # Trajektoria ruchu z użyciem RK-4
    plt.subplot(2, 1, 2)
    plt.plot(linear_trajectory_rk4[:, 0], linear_trajectory_rk4[:, 1], label='Ruch prostoliniowy')
    plt.plot(circular_trajectory_rk4[:, 0], circular_trajectory_rk4[:, 1], label='Ruch po okręgu')
    plt.plot(alternating_trajectory_rk4[:, 0], alternating_trajectory_rk4[:, 1], label='Naprzemienny ruch')
    plt.scatter(initial_state[0], initial_state[1], color='red', label='Początkowa pozycja', zorder=5)
    plt.xlabel('x_1')
    plt.ylabel('x_2')
    plt.title('Ruch z użyciem RK-4')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')

    plt.tight_layout()
    plt.show()


def inertial_member_response(u, T, dt):
    """Definicja funkcji reprezentującej człon inercyjny"""
    n = len(u)
    y = np.zeros(n)
    y[0] = 0  # Warunek początkowy

    for k in range(1, n):
        y[k] = y[k - 1] + (dt / T) * (u[k] - y[k - 1])

    return y


def euler_method(r, h, x0, y0, v, p):
    T = len(v)
    dt = 1  # krok czasowy

    x = np.zeros(T + 1)
    y = np.zeros(T + 1)

    x[0] = x0
    y[0] = y0

    for t in range(T):
        x[t + 1] = x[t] + dt * (r * x[t] - h * y[t] - p[t] * v[t])
        y[t + 1] = y[t] + dt * v[t]

    return x, y


def robot_model(x, w):
    """
    Funkcja modelująca ruch dwukołowego robota mobilnego.
    Args:
        x (array): Wektor stanu [x_1, x_2, x_3]
        w (array): Wektor sterowania [w_1, w_2]
    Returns:
        dx (array): Pochodne czasowe wektora stanu
    """
    dx = np.array([
        [np.cos(x[2]), 0],
        [np.sin(x[2]), 0],
        [0, 1]
    ]).dot(w)
    return dx


def simulate_motion(initial_state, control_input, duration, dt):
    """
    Funkcja symulująca ruch robota mobilnego.
    Args:
        initial_state (array): Początkowy stan robota [x_1, x_2, x_3]
        control_input (function): Funkcja generująca sterowanie w zależności od czasu
        duration (float): Czas trwania symulacji
        dt (float): Krok czasowy
    Returns:
        trajectory (array): Trajektoria ruchu robota
    """
    t = 0
    x = initial_state
    trajectory = [x]

    while t < duration:
        w = control_input(t)
        dx = robot_model(x, w)
        x = x + dx * dt
        trajectory.append(x)
        t += dt

    return np.array(trajectory)


def linear_motion_control(t):
    """
    Sterowanie dla ruchu prostoliniowego.
    Args:
        t (float): Czas
    Returns:
        w (array): Wektor sterowania [w_1, w_2]
    """
    return np.array([1.0, 0.0])


def circular_motion_control(t):
    """
    Sterowanie dla ruchu po okręgu.
    Args:
        t (float): Czas
    Returns:
        w (array): Wektor sterowania [w_1, w_2]
    """
    return np.array([1.0, np.pi / 4])  # Prędkość liniowa 1, prędkość obrotowa pi/4


def alternating_motion_control(t):
    """
    Sterowanie dla naprzemiennego ruchu prostoliniowego i po okręgu.
    Args:
        t (float): Czas
    Returns:
        w (array): Wektor sterowania [w_1, w_2]
    """
    if t % 2 < 1:
        return np.array([1.0, 0.0])  # Ruch prostoliniowy przez 1 sekundę
    else:
        return np.array([1.0, np.pi / 4])  # Ruch po okręgu przez 1 sekundę


def rk2_integration(x, w, dt):
    """
    Implementacja metody Rungego-Kutty drugiego rzędu (RK-2).
    Args:
        x (array): Wektor stanu [x_1, x_2, x_3]
        w (array): Wektor sterowania [w_1, w_2]
        dt (float): Krok czasowy
    Returns:
        x_next (array): Nowy stan robota po dokonaniu kroku czasowego dt
    """
    k1 = robot_model(x, w)
    k2 = robot_model(x + 0.5 * dt * k1, w)
    x_next = x + dt * k2
    return x_next


def rk4_integration(x, w, dt):
    """
    Implementacja metody Rungego-Kutty czwartego rzędu (RK-4).
    Args:
        x (array): Wektor stanu [x_1, x_2, x_3]
        w (array): Wektor sterowania [w_1, w_2]
        dt (float): Krok czasowy
    Returns:
        x_next (array): Nowy stan robota po dokonaniu kroku czasowego dt
    """
    k1 = robot_model(x, w)
    k2 = robot_model(x + 0.5 * dt * k1, w)
    k3 = robot_model(x + 0.5 * dt * k2, w)
    k4 = robot_model(x + dt * k3, w)
    x_next = x + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
    return x_next


def lab3():
    # task1()
    # task2()
    task3()
    task4()
    task5()


if __name__ == "__main__":
    lab3()
