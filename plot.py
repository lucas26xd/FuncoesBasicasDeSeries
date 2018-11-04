import matplotlib.pyplot as plt


def plot(x, y, x1, y1, c, x2 = 0, y2 = 0):
    # Plano
    plt.plot([0, 0], [-1, 9], 'k^-')
    plt.plot([-1, 9], [0, 0], 'k^-')

    # Primeiro ponto
    p1, = plt.plot([0, x], [0, y], 'ro-')
    # Segundo ponto
    p2, = plt.plot([0, x1], [0, y1], 'bo-')

    if c:
        # Terceiro ponto
        p3, = plt.plot([0, x2], [0, y2], 'go-')
        plt.legend((p1, p2, p3), (fr'$Z_1$ ({x}, {y})', fr'$Z_3$ ({x1:.3}, {y1:.3})', fr'$Z_4$ ({x2:.3}, {y2:.3})'))
    else:
        plt.legend((p1, p2), (fr'$Z_1$ ({x}, {y})', fr'$Z_3$ ({x1:.3}, {y1:.3})'))

    plt.title("Rotacionando pontos" + (fr"- Diferença = $Z_4 - Z_3$ = ({x2-x1:.2}, {y2-y1:.2})" if c else ""))
    plt.grid(True)
    plt.xlabel(r"$\Re(z)$ - Parte Real")
    plt.ylabel(r"$\Im(z)$ - Parte Imaginária")

    plt.show()
