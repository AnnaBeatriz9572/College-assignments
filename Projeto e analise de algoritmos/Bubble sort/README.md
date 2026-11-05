# Lista Encadeada com Bubble Sort em Python

**Projeto e Análise de Algoritmos I | Trabalho Acadêmico**

## 📌 Sobre o projeto

Este projeto foi desenvolvido como atividade acadêmica da disciplina de **Projeto e Análise de Algoritmos I**, com o objetivo de implementar uma lista simplesmente encadeada em Python e aplicar o algoritmo de ordenação **Bubble Sort**.

A implementação permite explorar conceitos fundamentais de estruturas de dados, manipulação de nós, referências e análise de complexidade de algoritmos.

Além das operações básicas de uma lista encadeada, o projeto apresenta diferentes cenários de teste para observar o comportamento do Bubble Sort e compreender seu funcionamento.

## 🎯 Objetivos

- Implementar uma lista simplesmente encadeada utilizando programação orientada a objetos.
- Desenvolver operações de inserção, remoção, busca e contagem de elementos.
- Implementar o algoritmo Bubble Sort para ordenação crescente.
- Permitir a visualização das trocas realizadas durante a ordenação.
- Analisar a complexidade computacional das operações implementadas.
- Testar o algoritmo com diferentes configurações de entrada.

## 🛠️ Tecnologias utilizadas

- **Linguagem:** Python 3
- **Paradigma:** Programação Orientada a Objetos (POO)
- **Estrutura de dados:** Lista Simplesmente Encadeada
- **Algoritmo de ordenação:** Bubble Sort

O projeto utiliza apenas recursos nativos do Python, sem necessidade de bibliotecas externas.

## 📂 Estrutura do repositório

```text
lista-encadeada-bubble-sort/
│
├── README.md
│
└── lista_encadeada.py
```

O arquivo `lista_encadeada.py` contém a implementação da estrutura de dados, do algoritmo de ordenação e dos casos de teste.

## ⚙️ Implementação

### 1. Estrutura da lista encadeada

Uma lista simplesmente encadeada é uma estrutura de dados linear composta por nós conectados por referências.

Cada nó contém:

- **valor:** informação armazenada.
- **proximo:** referência para o próximo nó da lista.

A classe `No` representa cada elemento da estrutura, enquanto a classe `ListaEncadeada` gerencia as operações realizadas sobre a lista.

Exemplo de representação:

```text
INÍCIO
  |
  v
[10 | •] -> [20 | •] -> [30 | None]
```

O último nó possui a referência `None`, indicando o fim da lista.

### 2. Operações implementadas

| Método | Descrição |
|---|---|
| `inserir_inicio(valor)` | Insere um nó no início da lista. |
| `inserir_final(valor)` | Adiciona um nó ao final da lista. |
| `remover_no(valor)` | Remove a primeira ocorrência do valor informado. |
| `imprimir_lista()` | Exibe os valores armazenados. |
| `busca_lista(valor)` | Verifica se determinado valor existe na lista. |
| `tamanho_lista()` | Retorna a quantidade de elementos. |
| `bubble_sort(visualizar=False)` | Ordena os elementos em ordem crescente. |

## 🔄 Algoritmo Bubble Sort

O **Bubble Sort** é um algoritmo de ordenação baseado na comparação de elementos adjacentes.

Durante sua execução, o algoritmo percorre a lista e troca os valores de dois nós consecutivos sempre que estiverem fora da ordem desejada.

Esse processo se repete até que todos os elementos estejam ordenados.

### Funcionamento

Considere a lista inicial:

```text
[5, 3, 8, 1]
```

Durante a primeira passagem:

```text
[5, 3, 8, 1]  →  Estado inicial

[3, 5, 8, 1]  →  Troca 5 e 3

[3, 5, 1, 8]  →  Troca 8 e 1
```

Ao final da primeira passagem, o maior elemento já estará na última posição.

Nas passagens seguintes, os elementos restantes continuarão sendo comparados até alcançar:

```text
[1, 3, 5, 8]
```

### Otimizações implementadas

A implementação utiliza duas estratégias para melhorar o funcionamento do Bubble Sort:

**1. Interrupção antecipada**

A variável `trocou` identifica se houve alguma troca durante a passagem. Caso nenhuma troca seja realizada, o algoritmo encerra sua execução, pois a lista já está ordenada.

**2. Redução das comparações**

A variável `passou_limite` identifica o início da região final já ordenada, evitando comparações desnecessárias com elementos que estão em suas posições definitivas.

**Observação:** a implementação realiza trocas entre os valores armazenados nos nós, sem modificar as referências que conectam a lista.

### Visualização das trocas

O método permite acompanhar a ordenação utilizando o parâmetro `visualizar`.

```python
lista.bubble_sort(visualizar=True)
```

Quando ativado, o programa imprime o estado da lista imediatamente após cada troca realizada.

Para executar a ordenação sem exibir as etapas intermediárias:

```python
lista.bubble_sort()
```

## 🧪 Casos de teste

Foram desenvolvidos três cenários para analisar o funcionamento do algoritmo em diferentes condições.

### Teste 1 — Lista com valores aleatórios

**Entrada:**

```text
[42, 7, 19, 3, 55, 22, 11]
```

**Saída esperada:**

```text
[3, 7, 11, 19, 22, 42, 55]
```

Nesse teste, a opção de visualização está ativada, permitindo acompanhar todas as trocas realizadas.

### Teste 2 — Lista quase ordenada

**Entrada:**

```text
[2, 3, 5, 4, 6, 8, 7, 10]
```

**Saída esperada:**

```text
[2, 3, 4, 5, 6, 7, 8, 10]
```

Esse cenário permite observar o comportamento do algoritmo quando poucos elementos estão fora de ordem.

### Teste 3 — Lista em ordem inversa

**Entrada:**

```text
[50, 40, 30, 20, 10, 5]
```

**Saída esperada:**

```text
[5, 10, 20, 30, 40, 50]
```

Nesse cenário, todos os elementos estão inicialmente em ordem decrescente, exigindo o maior número de trocas para ordenar essa lista.

## 📊 Análise de complexidade

A análise considera uma lista com `n` elementos.

### Complexidade das operações

| Operação | Complexidade de tempo |
|---|---|
| Inserção no início | O(1) |
| Inserção no final | O(n) |
| Remoção por valor | O(n) |
| Busca por valor | O(n) |
| Contagem de elementos | O(n) |
| Impressão da lista | O(n) |

Os valores da tabela representam a complexidade no pior caso.

### Complexidade do Bubble Sort

| Cenário | Complexidade de tempo |
|---|---|
| Melhor caso | O(n) |
| Caso médio | O(n²) |
| Pior caso | O(n²) |

**Melhor caso — O(n)**

Ocorre quando a lista já está ordenada. O algoritmo realiza uma passagem sem efetuar trocas e encerra sua execução.

**Caso médio — O(n²)**

Em uma entrada típica não ordenada, o algoritmo realiza múltiplas passagens, efetuando comparações e possíveis trocas.

**Pior caso — O(n²)**

Ocorre, por exemplo, quando os elementos estão organizados em ordem inversa à desejada, exigindo um número quadrático de comparações e trocas.

**Complexidade espacial:** O(1) para a ordenação sem visualização, pois o Bubble Sort utiliza apenas uma quantidade constante de variáveis auxiliares.

**Observação sobre a visualização:** com `visualizar=True`, cada troca chama o método `imprimir_lista()`, que percorre os `n` elementos. Por isso, considerando também essas impressões, o tempo no pior caso pode chegar a O(n³), e a memória auxiliar utilizada temporariamente passa a O(n).

## 🚀 Como executar

### Pré-requisitos

Ter o Python 3 instalado no computador.

### 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Acessar a pasta do projeto

```bash
cd lista-encadeada-bubble-sort
```

### 3. Executar o programa

```bash
python lista_encadeada.py
```

O programa executará automaticamente os três casos de teste e exibirá os resultados no terminal.

## 📚 Conceitos abordados

A atividade permite aplicar conhecimentos relacionados a:

- Estruturas de dados lineares.
- Listas simplesmente encadeadas.
- Programação Orientada a Objetos.
- Manipulação de referências entre nós.
- Algoritmos de busca e ordenação.
- Complexidade de tempo e espaço.
- Notação assintótica Big O.
- Análise experimental de algoritmos.

## 👥 Equipe

Projeto desenvolvido pelos integrantes:

- **Anna Beatriz Cardoso**
- **Luiz Felipe Fernandes**
- **Neemias Lôres**
- **Rayssa Rodrigues**
- **Yasmin Montes**

**Disciplina:** Projeto e Análise de Algoritmos I

## 📝 Considerações finais

O desenvolvimento deste projeto possibilitou compreender o funcionamento de uma lista simplesmente encadeada e a aplicação de um algoritmo de ordenação sobre essa estrutura.

A implementação do Bubble Sort, juntamente com os diferentes cenários de teste, permite observar como a organização inicial dos elementos influencia o número de comparações e trocas realizadas.

Embora o Bubble Sort não seja indicado para conjuntos de dados muito grandes devido à sua complexidade quadrática, sua implementação possui valor didático para o estudo de algoritmos de ordenação, estruturas de dados e análise de eficiência computacional.

---

*Projeto desenvolvido para fins acadêmicos e educacionais.*
