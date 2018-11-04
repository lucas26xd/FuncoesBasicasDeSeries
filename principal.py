from funcoes import exp, r, arctg
from plot import plot
from math import cos, sin, atan


def main():
    x = float(input("Coord. X = "))
    y = float(input("Coord. Y = "))
    a = float(input("Ang. Psi = "))

    N = 20  # 20 iterações para todas as séries

    x1, y1 = exp(r(x, y), a + arctg(x, y, N), N)

    print(f"(x', y') = ({x1}, {y1})")

    x2 = r(x, y) * cos((a / 180 * 3.141592654) + atan(y/x))
    y2 = r(x, y) * sin((a / 180 * 3.141592654) + atan(y/x))

    plot(x, y, x1, y1, False)
    plot(x, y, x1, y1, True, x2, y2)


if __name__ == "__main__":
    main()
