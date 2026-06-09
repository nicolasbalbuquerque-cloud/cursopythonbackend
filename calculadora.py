def executar_calculadora():
    print("====================================")
    print("   BEM-VINDO À CALCULADORA PYTHON   ")
    print("====================================")

    # Laço principal para permitir múltiplas operações
    while True:
        # 1. Exibição do Menu de Opções
        print("\nEscolha a operação desejada:")
        print("1 - Soma (+)")
        print("2 - Subtração (-)")
        print("3 - Multiplicação (*)")
        print("4 - Divisão (/)")
        print("5 - Sair do Programa")
        
        # 2. Captura da escolha do usuário
        opcao = input("\nDigite o número da opção (1-5): ").strip()

        # Verificação de saída imediata antes de solicitar os números
        if opcao == "5":
            break

        # Verificação preliminar se a opção digitada é válida
        if opcao not in ["1", "2", "3", "4"]:
            print("❌ Erro: Opção inválida! Por favor, escolha um número de 1 a 5.")
            continue  # Retorna ao início do laço para nova tentativa

        # 3. Solicitação dos operandos numéricos com conversão para Float
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("❌ Erro: Entrada inválida! Certifique-se de digitar números válidos.")
            continue

        # 4. Estrutura Condicional para Execução dos Cálculos
        if opcao == "1":
            resultado = num1 + num2
            print(f"\n➔ Resultado: {num1} + {num2} = {resultado}")

        elif opcao == "2":
            resultado = num1 - num2
            print(f"\n➔ Resultado: {num1} - {num2} = {resultado}")

        elif opcao == "3":
            resultado = num1 * num2
            print(f"\n➔ Resultado: {num1} * {num2} = {resultado}")

        elif opcao == "4":
            # 5. Tratamento de salvaguarda contra divisão por zero
            if num2 == 0:
                print("❌ Erro: Divisão por zero não é permitida no escopo dos números reais.")
            else:
                resultado = num1 / num2
                print(f"\n➔ Resultado: {num1} / {num2} = {resultado}")

        # 6. Funcionalidade de continuidade do loop
        continuar = input("\nDeseja realizar outra operação? (S/N): ").strip().upper()
        if continuar != "S":
            break

    # Mensagem de encerramento do script
    print("\n====================================")
    print(" Obrigado por usar a calculadora! ")
    print("         Até a próxima!             ")
    print("====================================")

# Ponto de entrada padrão para execução do script isolado
if __name__ == "__main__":
    executar_calculadora()