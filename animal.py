
# Classe-Mãe (Superclasse)
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        print("O animal emitiu um som genérico.")


# Classe-Filha (Subclasse) que herda de Animal
class Cachorro(Animal):
    # Sobrescrita do método emitir_som (Polimorfismo)
    def emitir_som(self):
        print("O cachorro latiu!")


# Outra Classe-Filha (Subclasse) que herda de Animal
class Gato(Animal):
    # Sobrescrita do método emitir_som (Polimorfismo)
    def emitir_som(self):
        print("O gato miou!")


# Programa Principal
def main():
    # 1. Criando os objetos (instanciando as subclasses)
    # Definindo os nomes e idades diretamente no construtor
    meu_cachorro = Cachorro(nome="Rex", idade=5)
    meu_gato = Gato(nome="Mingau", idade=3)

    # 2. Chamando o método emitir_som para ambos os objetos
    # Cada objeto responderá com seu próprio comportamento específico
    meu_cachorro.emitir_som()
    meu_gato.emitir_som()


# Ponto de execução padrão
if __name__ == "__main__":
    main()