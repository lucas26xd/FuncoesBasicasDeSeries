'''
Código desenvolvido para apresentação sobre Séries e Sequências
na disciplina de Variáveis Complexas - 2018.2
Autor: Lucas Santos.

n = número de iterações desejadas para cada série
x, y = par ordenado do ponto
theta = ângulo desejado de rotação

Este código tem a função de mostrar como implementei algumas funções básicas a partir de séries
e mostrar a rotação de um ponto usando a matriz de rotação complexa
'''


def fat(n):  # Retorna o fatorial de n
    if n == 0:
        return 1
    else:
        return fat(n - 1) * n


def seno(theta, n):  # Série que representa o valor do sen(theta)
    theta = theta * 3.141592654 / 180  # Conversão de graus para radianos
    sen = 0
    for i in range(0, n):
        sen = sen + (((-1) ** i) / fat((2 * i) + 1) * (theta ** ((2 * i) + 1)))
    return sen


def cosseno(theta, n):  # Série que representa o valor do cos(theta)
    theta = theta * 3.141592654 / 180  # Conversão de graus para radianos
    cos = 0
    for i in range(0, n):
        cos = cos + ((((-1) ** i) / fat(2 * i)) * (theta ** (2 * i)))
    return cos


def e(theta, n):  # Série que aproxima do valor da exponencial de theta
    e = 0
    for i in range(0, n):
        e = e + ((theta ** i) / fat(i))
    return e


def exp(r, x, n):  # Retorna uma tupla contendo as coordenadas do novo ponto
    return [r * cosseno(x, n), r * seno(x, n)]


def arctg(x, y, n):  # Série que aproxima o valor do arctg
    aux = False
    if x < y:  # Correção de erro para y > x
        aux = True
        x, y = y, x

    arctg = 0
    for i in range(0, n):
        arctg = arctg + ((((-1) ** i) / ((2 * i) + 1)) * (y / x) ** ((2 * i) + 1))

    if aux:
        arctg = (3.141592654/2) - arctg  # Correçãode erro para y > x

    return arctg * 180 / 3.141592654  # Conversão de radianos para graus


def arctan(x, y):  # Aproximação da série do arctan
    #return (y / x) - ((1 / 3) * ((y / x) ** 3)) + ((1 / 5) * ((y / x) ** 5))
    return arctg(x, y, 3)


def pi(n):  # Série que se aproxima o número PI = 3.141592654
    pi = 0
    for i in range(0, n):
        pi = pi + (((-1) ** i) / ((2 * i) + 1))
    return pi * 4


def r(x, y):  # Retorna o módulo do número complexo
    return ((x ** 2) + (y ** 2)) ** 0.5
