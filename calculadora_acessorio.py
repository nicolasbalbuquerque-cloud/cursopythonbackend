# Dicionário mapeando as operações para funções anônimas (lambda)
# Cada lambda recebe dois argumentos (x, y) e retorna o resultado da operação
operacoes = {
    "1": lambda x, y: x + y,
    "2": lambda x, y: x - y,
    "3": lambda x, y: x * y,
    "4": lambda x, y: x / y
}


def obter_numero(mensagem):
    """
    Solicita um número ao usuário e usa try-except para garantir 
    que apenas valores numéricos válidos sejam aceitos.
    """
    while True:
        try:
            return float(input(mensagem).strip())
        except ValueError:
            print("Erro: Valor inválido! Por favor, insira um número válido.")


def main():
    print("=== Bem-vindo à Calculadora Simples ===")
    
    while True:
        # 1. Coleta dos dois números iniciais com validação de tipo
        num1 = obter_numero("Insira o primeiro número: ")
        num2 = obter_numero("Insira o segundo número: ")
        
        # 2. Organização do menu usando List Comprehension
        # Gera dinamicamente a estrutura visual do menu baseada nos itens abaixo
        lista_opcoes = ["Soma", "Subtração", "Multiplicação", "Divisão"]
        menu_linhas = [f"{i+1} - {opcao}" for i, opcao in enumerate(lista_opcoes)]
        
        while True:
            print("\nEscolha uma operação:")
            # Exibe o menu gerado pela list comprehension linha por linha
            for linha in menu_linhas:
                print(linha)
                
            opcao = input("Escolha uma opção (1 a 4): ").strip()
            
            if opcao in operacoes:
                # Armazena o nome da operação escolhida para a mensagem de exibição
                nome_operacao = lista_opcoes[int(opcao) - 1]
                print(f"Você escolheu: {nome_operacao}")
                
                # 3. Tratamento específico para a divisão por zero (Opção 4)
                if opcao == "4":
                    while num2 == 0:
                        print("Divisão por zero não é permitida.")
                        num2 = obter_numero("Por favor, insira outro número (divisor): ")
                
                # Executa a função lambda correspondente passando os dois números
                resultado = operacoes[opcao](num1, num2)
                print(f"O resultado é: {resultado}")
                break  # Sai do loop de escolha da operação após calcular com sucesso
            else:
                print("Erro: Opção de operação inválida! Tente novamente.")
        
        # 4. Condição de parada do loop principal
        continuar = input("\nDeseja realizar outra operação? (S/N): ").strip().upper()
        if continuar != "S":
            print("Encerrando o programa... Obrigado por usar a calculadora!")
            break


if __name__ == "__main__":
    main()