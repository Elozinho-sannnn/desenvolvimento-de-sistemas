import random

print("1 - Nível fácil 1")
print("2 - Nível médio 2")
print("3 - Nível difícil 3")
opcao = int(input("Digite a opção desejada:"))
if (opcao == 1):
    numero_max = 10
    limite_tentativas = 5
elif (opcao == 2):
    numero_max = 10
    limite_tentativas = 3
elif (opcao == 3):
    numero_max = 10
    limite_tentativas = 2
else: 
    print( "Opção invália, selecionado modo facil")
    numero_max = 10
    limite_tentativas = 5


sorteio = random.randint(1, numero_max)
#print(sorteio)
print("### JOGO DA ADIVINHAÇÃO ###")
print("Adivinhe o número que estou pensando, de 1 a 10")
tentativa = 1
while (limite_tentativas >= tentativa):
    print("Tentativa", tentativa)
    chute = int(input("Digite o seu chute:"))
    if (chute == sorteio):
        print("Parabéns, você acertou!")
        break
    elif (chute > sorteio):
        print("Chute um número menor!")
    elif (chute < sorteio):
        print("Chute um número maior!")
    tentativa = tentativa + 1
    # FINAL DO LAÇO WHILE
print("O número sorteado era: ##", sorteio, "##")
print("### FIM DO JOGO ###")