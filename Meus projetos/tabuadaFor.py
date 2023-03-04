# Montar uma tabuada com o número que foi digitado pelo usuário
tabuada = int(input("Digite um número para exibir a tabuada: "))
print("T A B U A D A")
for numero in range(1, 11, 1):
    print(tabuada, "x", numero, "=", tabuada*numero)