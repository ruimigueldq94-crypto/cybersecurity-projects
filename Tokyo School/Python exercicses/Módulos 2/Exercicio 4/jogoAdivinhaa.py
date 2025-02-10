import random

# Função principal do jogo da adivinha
def jogo_adivinha():
    # Gerar um número secreto aleatório entre 1 e 100
    # Foi proposta a solução em Java: int numeroAleatorio = (int) (Math.random() * 100 + 1);
    # Como eu faço em Python, tem de ficar algo assim: 
    numero_secreto = random.randint(1, 100)
    tentativas = 7

    print("Bem-vindo ao Jogo da adivinha!")
    print("Tente adivinhar o número secreto entre 1 e 100.")
    print(f"Você tem {tentativas} tentativas.")

    # Loop para as tentativas do utilizador
    while tentativas > 0:
        try:
            # Solicitar palpite do utilizador
            palpite = int(input("Escreva seu palpite: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        # Verificar se o palpite está correto
        if palpite == numero_secreto:
            print(f"Parabéns! Você adivinhou o número secreto {numero_secreto} em {7 - tentativas + 1} tentativas!")
            break
        elif palpite < numero_secreto:
            print("O número secreto é maior.")
        else:
            print("O número secreto é menor.")

        # Diminuir o número de tentativas
        tentativas -= 1
        print(f"Você tem {tentativas} tentativas restantes.")

    # Se o utilizador ficar sem tentativas, revelar o número secreto
    if tentativas == 0:
        print(f"Você ficou sem tentativas. O número secreto era {numero_secreto}.")

# Executar o programa principal
if __name__ == "__main__":
    jogo_adivinha()
