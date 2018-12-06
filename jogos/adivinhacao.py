print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 43

# chute_str = input("Digite o seu número: ")
# chute = int(chute_str)
chute = int(input("Digite o seu número: "))

print("Você digitou:", chute)

if (numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você errou!")

print("Fim de jogo")