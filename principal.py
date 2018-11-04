from funcoes import seno, cosseno, exp, arctg, r, arctan
from plot import plot


def main():
    x = float(input("Coord. X = "))
    y = float(input("Coord. Y = "))
    a = float(input("Ang. Psi = "))

    N = 20  # 20 iterações para todas as séries

    x1, y1 = exp(r(x, y), a + arctg(x, y, N), N)

    print(f"(x', y') = ({x1}, {y1})")

    plot(x, y, x1, y1)


if __name__ == "__main__":
    main()
