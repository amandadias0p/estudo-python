#programa que lê nome, idade, sexo de 4 pessoas e no final mostre a média de idade do grupo, o nome do homem mais velho e quantas mulheres tem menos de 20 anos

idadeMaisVelho = 0
somaIdade = 0
nomeMaisVelho = ""
totalMulher20 = 0

for pessoa in range(1, 5, 1):
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    genero = str(input("Sexo [M/F]: ").upper())
    somaIdade = somaIdade + idade
    if idade > idadeMaisVelho and genero == "M":
        idadeMaisVelho = idade
        nomeMaisVelho = nome
    if genero == "F" and idade < 20:
        totalMulher20 = totalMulher20 + 1
media = somaIdade/4
print("A média de idade do grupo é", media)
print("O homem mais velho é", nomeMaisVelho, "e tem", idadeMaisVelho, "anos")
print("Temos", totalMulher20, "mulheres com menos de 20 anos")
