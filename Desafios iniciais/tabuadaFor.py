# Montar uma tabuada com o número que foi digitado pelo usuário
tabuada = int(input("Digite um número para exibir a tabuada: "))
print("Tabuada do número", tabuada)
for numero in range(1, 11, 1):
    print(tabuada, "x", numero, "=", tabuada*numero)