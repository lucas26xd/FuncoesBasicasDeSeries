import matplotlib.pyplot as plt


def plot(x, y, x1, y1):
    # Plano
    plt.plot([0, 0], [-1, 9], 'k^-')
    plt.plot([-1, 9], [0, 0], 'k^-')

    # Primeiro ponto
    p1, = plt.plot([0, x], [0, y], 'ro-')
    # Segundo ponto
    p2, = plt.plot([0, x1], [0, y1], 'bo-')

    plt.legend((p1, p2), (fr'$Z_1$ ({x}, {y})', fr'$Z_3$ ({x1:.3}, {y1:.3})'))

    plt.title("Rotacionando pontos")
    plt.grid(True)
    plt.xlabel(r"$\Re(z)$ - Parte Real")
    plt.ylabel(r"$\Im(z)$ - Parte Imaginária")

    plt.show()
