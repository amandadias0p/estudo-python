#Utilizar while para o processo, de forma que, caso o paciente responda com algo diferente de "sim" e "nao", o código continue perguntando se o paciente tem suspeita de doença infectocontagiosa

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
if idade >= 65:
    print("Paciente COM prioridade!")
else:
    genero = input("Digite o gênero (M/F): ").upper()
    if genero == "F" and idade > 10:
        gravidez = input("Você está grávida? (SIM/NAO) ").upper()
        if gravidez == "SIM":
            print("Paciente COM prioridade!")
        else:
            print("Paciente SEM prioridade")
    else:
        print("Paciente SEM prioridade!")

doencaContagiosa = input("O paciente suspeita de alguma doença infectocongiosa? (SIM/NAO) ").upper()
while doencaContagiosa != "SIM" and doencaContagiosa!= "NAO":
    input("Por favor, responda com SIM ou NAO!")
    doencaContagiosa = input("O paciente suspeita de alguma doença infectocongiosa? ").upper()


if doencaContagiosa == "SIM":
    print("Encaminhe o paciente para a sala AMARELA!")
else:
    print("Encaminhe o paciente para a sala BRANCA!")
