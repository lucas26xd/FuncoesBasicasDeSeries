from fatorial import fat

x = float(input("COS "))
n = int(input("Entre com o tamanho de n: "))

cos = 0
for i in range(0, n):
    cos = cos + ((((-1) ** i) / fat(2 * i)) * (x ** (2 * i)))

print(f"COS({x}) = {cos:.2}")