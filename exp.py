from fatorial import fat

x = float(input("EXP "))
n = int(input("Entre com o tamanho de n: "))

exp = 0
for i in range(0, n):
    exp = exp + ((x ** i) / fat(i))

print(f"EXP({x}) = {exp}")
