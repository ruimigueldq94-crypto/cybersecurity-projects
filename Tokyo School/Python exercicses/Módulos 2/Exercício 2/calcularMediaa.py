# Método para calcular a média de três notas
def calcularMedia(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

# Método para contar o número de palavras numa frase
def contarPalavras(frase):
    palavras = frase.split()  # Divide a frase em palavras
    return len(palavras)

# Programa principal
def main():
    print("Bem-vindo à Calculadora de Média!")

    # Solicitar ao utilizador que insira três notas
    nota1 = float(input("Escreva a primeira nota: "))
    nota2 = float(input("Escreva a segunda nota: "))
    nota3 = float(input("Escreva a terceira nota: "))

    # Calcular a média das notas
    media = calcularMedia(nota1, nota2, nota3)

    # Exibir o resultado da média
    print(f"A média das três notas é: {media:.2f}")

    # Solicitar ao utilizador que insira uma frase
    frase = input("Escreva uma frase para exibir o número de palavras: ")

    # Contar o número de palavras na frase
    numero_de_palavras = contarPalavras(frase)

    # Exibir o número de palavras
    print(f"O número de palavras na frase é: {numero_de_palavras}")

# Executar o programa principal
if __name__ == "__main__":
    main()
