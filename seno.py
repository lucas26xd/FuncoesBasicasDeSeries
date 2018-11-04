from fatorial import fat

def seno(x, n):
    sen = 0
    for i in range(0, n):
        sen = sen + (((-1) ** i) / fat((2 * i) + 1) * (x ** ((2 * i) + 1)))
    return sen
