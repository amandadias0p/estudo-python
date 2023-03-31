num = int(input("Digite um número: "))

#Descobrir se o número é par
if (num%2) == 0:
    print("O número é par!")
else:
    print("O número é ímpar!")

#Descobrir se o número é maior, igual ou menor do que 10
if num >= 10:
    if num == 10:
        print("O número é 10!")
    else:
        print("O número é maior do que 10!")
else:
    print("O número é menor do que 10!")

#Mostrar o dobro do número
dobro = num*2
print("O dobro do número digitado é", dobro)

#Descobrir se o número é primo
numerosDivididos = 0
contadorDivisao = 0
while numerosDivididos <= num:
    numerosDivididos += 1
    if num%numerosDivididos == 0:
        contadorDivisao += 1
print("Ao todo, existem", contadorDivisao, "valores divisíveis")
if contadorDivisao > 2:
    print("Ou seja, esse número não é primo!")
else:
    print("Ou seja, esse número é primo!")