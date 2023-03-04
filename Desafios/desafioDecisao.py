# o módulo deve pedir o nível de acesso de uma pessoa, que pode ser: ADM, USR ou GUEST, e o gênero dessa pessoa. Caso o nível seja ADM, deve exibir "Olá administrador" para os homens ou "Olá administradora" para as mulheres. Se o nível for USR deve exibir "Olá usuário" para os homens e "Olá usuária" para as mulheres. Se o nível for GUEST, a mensagem deverá ser "Olá visitante". E se o nível digitado for diferente de ADM, USR ou GUEST, deverá exibir a mensagem "Olá desconhecido(a)".
nivel = (input("Digite o nível de acesso (ADM, USR ou GUEST): ")).upper()
if nivel == "ADM" or nivel == "USR":
    genero = input("Digite o gênero (F ou M):").upper()
    if nivel == "ADM":
        if genero == "F":
            print("Olá administradora!")
        else:
            print("Olá administrador")
    elif genero == "F":
        print("Olá usuária!")
    else:
        print("Olá usuário!")
elif nivel == "GUEST":
    print("Olá visitante!")
else:
    print("Olá desconhecido(a)!")
    