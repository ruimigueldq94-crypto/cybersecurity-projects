# Programa para armazenar e apresentar informações básicas sobre um estudante

# Solicitar o nome do estudante e armazenar na variável 'nome'
nome = input("Escreva o nome do estudante: ")

# Solicitar a idade do estudante, converter para inteiro e armazenar na variável 'idade'
idade = int(input("Escreva a idade do estudante: "))

# Solicitar a nota do estudante no exame, converter para float e armazenar na variável 'nota'
nota = float(input("Escreva a nota do estudante no exame: "))

# Exibe os dados do estudante formatados de forma adequada
print("\nInformações do Estudante:")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Nota no exame: {nota:.2f}")  # Formatar a nota para duas casas decimais
