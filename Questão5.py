"""Crie uma lista contendo dicionários de produtos de forma a representar"""

produtos =  [
    {
        "produto": "Lápis",
        "preco": 5.54
    },
    {
        "produto": "Caneta",
        "preco": 7.25
    }
]

print(f"{produtos[0]["produto"]} - R$ {produtos[0]["preco"]}")
print(f"{produtos[1]["produto"]} - R$ {produtos[1]["preco"]}")