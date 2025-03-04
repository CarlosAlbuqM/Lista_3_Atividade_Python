""" Crie um programa em Python  que leia um valor inteiro e exiba todos os números pares e ímpares no intervalo de 1 a esse valor, separando-os"""

par = []
impar = []
numero = int(input("Digite um valor inteiro:"))

for i in range(1, numero+1, 1):
    if i % 2 == 0:
        par.append(i)
    elif i % 2 != 0:
        impar.append(i)


print(f"Números pares até {numero}: {par}")

print(f"Números ímpares até {numero}: {impar}")