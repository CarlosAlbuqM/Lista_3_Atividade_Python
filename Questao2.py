""" Desenvolva um algoritimo em python que receba 3 notas e faça a média."""

n1 = float(input("Digite a nota da primeira unidade: "))
n2 = float(input("Digite a nota da segunda unidade: "))
n3 = float(input("Digite a nota da terceira unidade: "))

media = (n1+n2+n3) / 3

if media >= 7:
    print("Aprovado")
elif media < 7 and media >= 4:
    print("Reposição")
else:
    print("Reprovado")