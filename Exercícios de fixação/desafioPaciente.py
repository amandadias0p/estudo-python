#Caso o paciente tenha 65 anos ou mais, deve ter atendimento prioritário. Se houver suspeita de doença contagiosa, deve ir para a sala amarela. Caso seja mulher e estiver grávida, também tem direito ao atendimento prioritário. Outros casos seguirão para a sala branca e terão atendimento comum

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

doençaContagiosa = input("O paciente apresenta suspeita de doença contagiosa? (SIM/NAO) ").upper()
if doençaContagiosa == "SIM":
    print("Encaminhe o paciente para a sala AMARELA!")
elif doençaContagiosa == "NAO":
    print("Encaminhe o paciente para a sala BRANCA!")
else:
    print("Por favor, responda a pergunta com SIM ou NAO")
