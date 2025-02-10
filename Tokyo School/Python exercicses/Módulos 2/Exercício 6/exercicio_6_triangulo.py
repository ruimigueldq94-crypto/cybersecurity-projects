import math

def calcular_area(ladoA, ladoB, ladoC):
    # Fórmula para a área de um triângulo
    semi_perimetro = (ladoA + ladoB + ladoC) / 2
    area = math.sqrt(semi_perimetro * (semi_perimetro - ladoA) * (semi_perimetro - ladoB) * (semi_perimetro - ladoC))
    return area

def calcular_angulos(ladoA, ladoB, ladoC):
    # Calcular os ângulos
    anguloA = math.degrees(math.acos((ladoB**2 + ladoC**2 - ladoA**2) / (2 * ladoB * ladoC)))
    anguloB = math.degrees(math.acos((ladoA**2 + ladoC**2 - ladoB**2) / (2 * ladoA * ladoC)))
    anguloC = math.degrees(math.acos((ladoA**2 + ladoB**2 - ladoC**2) / (2 * ladoA * ladoB)))
    return anguloA, anguloB, anguloC

def tipo_triangulo(ladoA, ladoB, ladoC):
    # Determinar o tipo de triângulo
    if ladoA == ladoB == ladoC:
        return "equilátero"
    elif ladoA == ladoB or ladoB == ladoC or ladoA == ladoC:
        return "isósceles"
    else:
        return "escaleno"

def eh_triangulo_valido(ladoA, ladoB, ladoC):
    # Verificar se os lados formam um triângulo válido
    return (ladoA + ladoB > ladoC) and (ladoA + ladoC > ladoB) and (ladoB + ladoC > ladoA)

# Programa principal
print("Bem-vindo à Calculadora de Triângulos.")

while True:
    print("\nEscolha uma opção:")
    print("1. Calcular a área do triângulo")
    print("2. Calcular os ângulos do triângulo")
    print("3. Sair")
    opcao = input("Escolha 1, 2 ou 3: ")

    if opcao == "3":
        print("Encerrando o programa. Obrigado!")
        break

    ladoA = float(input("Insira o comprimento do lado A: "))
    ladoB = float(input("Insira o comprimento do lado B: "))
    ladoC = float(input("Insira o comprimento do lado C: "))

    if not eh_triangulo_valido(ladoA, ladoB, ladoC):
        print("Os valores inseridos não formam um triângulo válido. Tente novamente.")
        continue

    tipo = tipo_triangulo(ladoA, ladoB, ladoC)
    print(f"O triângulo é do tipo: {tipo.capitalize()}.")

    if opcao == "1":
        area = calcular_area(ladoA, ladoB, ladoC)
        print(f"A área do triângulo é: {area:.2f}")

    elif opcao == "2":
        anguloA, anguloB, anguloC = calcular_angulos(ladoA, ladoB, ladoC)
        print(f"Os ângulos do triângulo são: A = {anguloA:.2f}°, B = {anguloB:.2f}°, C = {anguloC:.2f}°")

    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")
    
    # Perguntar ao user se ele quer realizar outra operação
    repetir = input("\nDeseja realizar outra operação? (s/n): ").strip().lower()
    if repetir != 's':
        print("Encerrando o programa. Obrigado!")
        break
