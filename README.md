# Curso Python Backend - Atividades de Versionamento

Este repositório contém o conjunto de aplicações práticas desenvolvidas em Python para consolidar conceitos de Programação Orientada a Objetos (POO), estruturas de dados, controle de fluxo e manipulação de dicionários.

O projeto foi estruturado seguindo as boas práticas de versionamento utilizando Git e GitHub, incluindo o fluxo de trabalho com ramificações (*branches*) e simulação de *Pull Requests*.

---

## Funcionalidades e Scripts Desenvolvidos

### 1. Sistema de Classes Animais (`animal.py`)
Aplica os pilares fundamentais da Programação Orientada a Objetos (POO):
- **Herança:** As subclasses `Cachorro` e `Gato` herdam propriedades da superclasse `Animal`.
- **Polimorfismo:** Sobrescrita do método `emitir_som()` para que cada animal responda com seu comportamento específico.

### 2. Calculadora Convencional (`calculadora.py`)
Uma aplicação interativa de terminal estruturada com laços de repetição e blocos condicionais que realiza operações aritméticas básicas com tratamento preventivo contra erros de entrada (`ValueError`) e divisões por zero.

### 3. Calculadora Avançada (`calculadora_acessorio.py`)
Evolução da calculadora comum utilizando recursos avançados da linguagem Python:
- Mapeamento de operações por meio de estruturas de dicionários.
- Utilização de funções anônimas (`lambda`).
- Criação visual de menus de forma dinâmica utilizando *List Comprehension*.

### 4. Gerenciador de Estoque (`gerenciador_estoque.py`)
Um CRUD completo em terminal para controle de inventário mercantil utilizando dicionários globais aninhados. Permite adicionar produtos com preço e quantidade, atualizar dados, remover itens e listar o estoque ordenado alfabeticamente usando a função `sorted()`.

---

## Como Executar as Aplicações

Certifique-se de ter o Python 3.10 ou superior instalado em sua máquina.

1. Escolha o script que deseja testar.
2. Execute o comando correspondente diretamente no seu terminal:

```bash
# Para testar o script de POO
python animal.py

# Para testar a calculadora padrão
python calculadora.py

# Para testar a calculadora com lambdas
python calculadora_acessorio.py

# Para testar o sistema de estoque
python gerenciador_estoque.py
