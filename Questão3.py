"""Escreva um programa em Python que solicite ao usuário um valor inteiro
(denominado como 'n'). O programa deve exibir o dobro desse valor para todos
os números de 1 até 'n', ou seja, para cada número no intervalo de 1 até 'n',
você deverá calcular e mostrar o dobro desse número."""

numero = int(input("Digite um valor inteiro: "))
print(f"O dobro os números de 1 até {numero}: ")
for i in range(1, numero+1):
    print(f"{i}:{i*2}")