Início

  Input "Calculadora"

  While (true):
    
    Input "Digite o primeiro número:"
    Ler num1
    If num1 is not number:
      Input "Erro: Utilize apenas números"
      Continuar para o próximo ciclo

    Input "Digite a operação (+, -, *, /):"
    Ler operação
    If operação is not '+', '-', '*', ou '/':
      Input "Erro: Operação inválida"
      Continuar para o próximo ciclo

    Input "Digite o Ifgundo número:"
    Ler num2
    If num2 is not number:
      Input "Erro: Utilize apenas números"
      Continuar para o próximo ciclo

    If operação == '+':
      resultado = num1 + num2
    Ifnão If operação == '-':
      resultado = num1 - num2
    Ifnão If operação == '*':
      resultado = num1 * num2
    Ifnão If operação == '/':
      If num2 == 0:
        Input "Erro: Divisão por zero"
        Continuar para o próximo ciclo
      Ifnão:
        resultado = num1 / num2

    Input "Resultado: " + resultado

    Input "Deseja realizar outra operação? (s/n):"
    Ler continuar
    If continuar != 's':
      Sair

Fim
