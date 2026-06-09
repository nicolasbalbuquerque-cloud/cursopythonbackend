# Dicionário global para armazenar o estoque
# Estrutura esperada: {"Nome": {"quantidade": int, "preço": float}}
estoque = {}


def adicionar_produto():
    print("\n--- Adicionar Produto ---")
    nome = input("Digite o nome do produto: ").strip()
    
    if nome in estoque:
        print(f"Erro: O produto '{nome}' já está cadastrado. Use a opção de atualizar.")
        return

    try:
        quantidade = int(input(f"Digite a quantidade de '{nome}': "))
        preco = float(input(f"Digite o preço de '{nome}': R$ "))
        
        # Criando o dicionário aninhado para o produto
        estoque[nome] = {
            "quantidade": quantidade,
            "preço": preco
        }
        print(f"Produto '{nome}' adicionado com sucesso!")
    except ValueError:
        print("Erro: Quantidade deve ser um número inteiro e preço um número decimal.")


def listar_products():
    print("\n--- Lista de Produtos em Estoque ---")
    if not estoque:
        print("O estoque está vazio.")
        return

    # Ordenando o estoque em ordem alfabética pelas chaves (nomes dos produtos)
    # O método estoque.items() retorna tuplas (chave, valor). 
    # A função lambda pega o elemento x (a tupla) e usa x[0] (a chave/nome do produto) para ordenar.
    produtos_ordenados = sorted(estoque.items(), key=lambda x: x[0])

    for nome, dados in produtos_ordenados:
        print(f"Nome do produto: {nome} - Quantidade disponível: {dados['quantidade']} - Preço: R$ {dados['preço']:.2f}")


def remover_produto():
    print("\n--- Remover Produto ---")
    nome = input("Digite o nome do produto a ser removido: ").strip()
    
    if nome in estoque:
        del estoque[nome]
        print(f"Produto '{nome}' removido com sucesso!")
    else:
        print(f"Erro: O produto '{nome}' não foi encontrado no estoque.")


def atualizar_quantidade():
    print("\n--- Atualizar Quantidade ---")
    nome = input("Digite o nome do produto: ").strip()
    
    if nome in estoque:
        try:
            nova_qtd = int(input(f"Digite a nova quantidade para '{nome}': "))
            # Atualiza apenas o valor da chave "quantidade" dentro do sub-dicionário
            estoque[nome]["quantidade"] = nova_qtd
            print(f"Quantidade de '{nome}' atualizada para {nova_qtd} com sucesso!")
        except ValueError:
            print("Erro: A quantidade deve ser um número inteiro válido.")
    else:
        print(f"Erro: O produto '{nome}' não foi encontrado no estoque.")


def exibir_menu():
    print("\n========= MENU DE ESTOQUE =========")
    print("1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Remover produto")
    print("4 - Atualizar quantidade de produto")
    print("5 - Sair")
    print("====================================")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            listar_products()
        elif opcao == "3":
            remover_produto()
        elif opcao == "4":
            atualizar_quantidade()
        elif opcao == "5":
            print("Saindo do programa... Estoque encerrado.")
            break
        else:
            print("Opção inválida! Por favor, escolha um número de 1 a 5.")


if __name__ == "__main__":
    main()