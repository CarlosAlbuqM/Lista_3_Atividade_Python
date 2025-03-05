""" Convertor  de Temperaturas """

print ("\n\n Bem-vindo ao Conversor de Temperaturas! \n\n")

opcao = int(input("Escolha uma opção: \n 1. Converter de Celcius para Fahrenheit \n 2. Converter de Fahrenheit para Celsius \n"))

if opcao == 1:
    temperaturaC = int(input("Digite a temperatura em Celcius: "))
    celciustoF = (temperaturaC * 9/5) + 32
    print(f"{temperaturaC} graus em Celcius é igual a {celciustoF} graus Fahrenheit.")

elif opcao == 2:
    temperaturaF = int(input("Digit a temperatua em Fahrenheit: "))
    fahrenheittoC = (temperaturaF - 32) * 5/9
    print(f"{temperaturaF} graus em Fahrenheit é igual a {fahrenheittoC:.2f} graus Celcius.")
