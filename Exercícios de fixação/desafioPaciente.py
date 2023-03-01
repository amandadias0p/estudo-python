#Caso o paciente tenha 65 anos ou mais, deve ter atendimento prioritário. Se houver suspeita de doença contagiosa, deve ir para a sala amarela. Caso seja mulher e estiver grávida, também tem direito ao atendimento prioritário. Outros casos seguirão para a sala branca e terão atendimento comum

nome = input("Digite o nome: ")
genero = input("Digite o gênero (M/F): ").upper()
idade = int(input("Digite a idade: "))
if idade >= 65:
    print("Paciente com prioridade!")
elif genero == "F":
    if idade > 10:
        gravidez = input("Você está grávida? (SIM/NAO): ")
        if gravidez == "SIM":
            print("Paciente com prioridade!")
        else:
            print("Paciente sem prioridade!")
    else:
        print("Paciente sem prioridade!")
else:
    print("Paciente sem prioridade!")

doençaContagiosa = input("O paciente apresenta suspeita de doença contagiosa? (SIM/NAO) ").upper()
if doençaContagiosa == "SIM":
    print("Encaminhe o paciente para a sala AMARELA!")
elif doençaContagiosa == "NAO":
    print("Encaminhe o paciente para a sala BRANCA!")
else:
    print("Por favor, responda a pergunta com SIM ou NAO")
