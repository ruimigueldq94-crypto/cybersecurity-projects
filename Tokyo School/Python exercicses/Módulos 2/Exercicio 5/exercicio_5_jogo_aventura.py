import random

# Função principal
def jogo_aventura():
    # Introdução da história
    print("Bem-vindo ao Jogo de Aventura!")
    print("Você é um explorador à procura de um tesouro lendário numa ilha misteriosa.")
    print("Prepare-se para enfrentar perigos e tomar decisões que afetarão o seu destino.\n")

    # Variável para controlar o fim do jogo
    fim_de_jogo = False

    while not fim_de_jogo:
        # Cenário inicial
        print("Você desembarca na ilha e tem duas opções de caminho à sua frente.")
        print("1. Entrar na selva densa")
        print("2. Seguir trilho costeiro")
        print("3. Sair do jogo")
        escolha1 = input("Escolha 1, 2 ou 3: ")

        # Primeira decisão
        if escolha1 == "1":
            print("\nVocê aventura-se na selva densa...")
            print("A vegetação é fechada, e o som dos animais selvagens está ao seu redor.")
            print("Você depara-se com um rio caudal bloqueando o caminho.")
            print("1. Tentar atravessar o rio a nado")
            print("2. Procurar outra passagem")
            escolha2 = input("Escolha 1 ou 2: ")

            if escolha2 == "1":
                print("\nVocê tenta nadar através do rio, mas a corrente é muito forte.")
                print("Infelizmente, você é arrastado pela água e não consegue sobreviver.")
                print("Fim de jogo.")
                fim_de_jogo = True  # Finaliza o jogo

            elif escolha2 == "2":
                print("\nVocê segue a margem do rio e encontra uma ponte improvisada.")
                print("Ao cruzar a ponte, você encontra uma cabana abandonada!")
                print("Você descansa, recupera forças e continua a explorar a ilha.")
                # O jogo continua

        elif escolha1 == "2":
            print("\nVocê segue o trilho costeiro, sentindo a brisa do mar.")
            print("Chega a uma caverna escura.")
            print("1. Entrar na caverna")
            print("2. Continuar pela costa")
            escolha2 = input("Escolha 1 ou 2: ")

            if escolha2 == "1":
                print("\nVocê acende uma tocha e entra na caverna escura...")
                print("Lá dentro, você encontra sinais de uma antiga civilização.")
                print("No fundo da caverna, você encontra um baú com o tesouro lendário!")
                print("Parabéns! Você encontrou o tesouro e completou a sua aventura!")
                fim_de_jogo = True  # Finaliza o jogo

            elif escolha2 == "2":
                print("\nVocê decide não entrar na caverna e continua pela costa.")
                print("Eventualmente, você chega a uma praia deserta onde está um barco ancorado.")
                print("Você usa o barco para escapar da ilha, mas sem o tesouro.")
                print("Fim de jogo.")
                fim_de_jogo = True  # Finaliza o jogo

        elif escolha1 == "3":
            print("Você decidiu sair da aventura. Até a próxima!")
            fim_de_jogo = True  # Finaliza o jogo

        else:
            print("Escolha inválida. Tente novamente.")

# Executar o jogo de aventura
if __name__ == "__main__":
    jogo_aventura()