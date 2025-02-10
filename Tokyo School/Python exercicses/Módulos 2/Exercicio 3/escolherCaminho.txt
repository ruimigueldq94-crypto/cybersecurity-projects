import random

# Método para escolher um caminho e receber uma resposta com base na escolha
def escolherCaminho():
    print("Bem-vindo à Escolha do Caminho!")
    print("Escolha um dos caminhos:")
    print("A. Caminho A")
    print("B. Caminho B")
    print("C. Caminho C")

    caminho = input("Escreva a letra correspondente ao caminho escolhido (A, B, C): ").strip().upper()

    if caminho == "A":
        print("Escolheu o Caminho A: É um caminho seguro e tranquilo!")
    elif caminho == "B":
        print("Escolheu o Caminho B: Este caminho é cheio de desafios!")
    elif caminho == "C":
        print("Escolheu o Caminho C: Este caminho é misterioso e desconhecido!")
    else:
        print("Opção inválida. Por favor, escolha as opções possíves: A, B ou C.")

# Método para adivinhar o número secreto
def adivinharNumero():
    numero_secreto = random.randint(1, 100)
    tentativas = 5

    print("Bem-vindo ao Jogo de adivinhar o numero de tentativas!")
    print("Tente adivinhar o número secreto entre 1 e 100.")
    print(f"Você tem {tentativas} tentativas.")

    for tentativa in range(1, tentativas + 1):
        palpite = int(input(f"Tentativa {tentativa}: Escreva seu palpite: "))

        if palpite < numero_secreto:
            print("O número secreto é maior.")
        elif palpite > numero_secreto:
            print("O número secreto é menor.")
        else:
            print(f"Parabéns! Você adivinhou o número secreto {numero_secreto} em {tentativa} tentativas!")
            break
    else:
        print(f"Você não conseguiu adivinhar o número secreto. O número era {numero_secreto}.")

# Programa principal
def main():
    escolherCaminho()
    adivinharNumero()

# Executar o programa principal
if __name__ == "__main__":
    main()
