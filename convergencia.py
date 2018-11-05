def fat(n):  # Retorna o fatorial de n
    if n == 0:
        return 1
    else:
        return fat(n - 1) * n


def seno(theta, n):  # Série que representa o valor do sen(theta)
    theta = theta * 3.141592654 / 180  # Conversão de graus para radianos

    print(30*'-')

    sen = 0
    for i in range(0, n):
        sen = sen + (((-1) ** i) / fat((2 * i) + 1) * (theta ** ((2 * i) + 1)))
        print(i, '-', sen)

    print(30 * '-')
    return sen


def cosseno(theta, n):  # Série que representa o valor do cos(theta)
    theta = theta * 3.141592654 / 180  # Conversão de graus para radianos

    print(30 * '-')

    cos = 0
    for i in range(0, n):
        cos = cos + ((((-1) ** i) / fat(2 * i)) * (theta ** (2 * i)))
        print(i, '-', cos)

    print(30 * '-')
    return cos

def e(theta, n):  # Série que aproxima do valor da exponencial de theta
    print(30 * '-')

    e = 0
    for i in range(0, n):
        e = e + ((theta ** i) / fat(i))
        print(i, '-', e)

    print(30 * '-')
    return e


def main():
    print('Entre com a função que deseja calcular')
    print('1=SEN, 2=COS, 3=EXP')
    f = int(input("f = "))

    print('Opção escolhida', 'Sen(x)' if f == 1 else 'Cos(x)' if f == 2 else 'Exp(x)')
    x = float(input('x = '))
    n = 20

    print('Sen(x)' if f == 1 else 'Cos(x)' if f == 2 else 'Exp(x)', '= ', end='')
    if f == 1:
        print(seno(x, n))
    elif f == 2:
        print(cosseno(x, n))
    else:
        print(e(x, n))


if __name__ == "__main__":
    main()
