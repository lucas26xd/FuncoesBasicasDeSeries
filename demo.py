from funcoes import seno, cosseno, e

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
