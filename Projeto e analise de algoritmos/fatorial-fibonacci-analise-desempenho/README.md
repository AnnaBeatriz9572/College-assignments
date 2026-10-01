# 📊 Análise Experimental de Algoritmos

## 📌 Sobre o projeto

Este projeto foi desenvolvido para a disciplina de **Projeto e Análise de Algoritmos**, da **Pontifícia Universidade Católica de Goiás (PUC Goiás)**.

O objetivo é analisar experimentalmente o desempenho de algoritmos **recursivos** e **iterativos**, comparando seus tempos de execução e relacionando os resultados obtidos com suas respectivas complexidades assintóticas.

Foram implementadas e comparadas duas versões dos algoritmos de **Fatorial** e **Fibonacci**:

- Fatorial recursivo;
- Fatorial iterativo;
- Fibonacci recursivo;
- Fibonacci iterativo.

---

## 🎯 Objetivo

Compreender, na prática, o comportamento de algoritmos recursivos e iterativos, analisando seus tempos de execução e comparando os resultados experimentais com a complexidade teórica.

---

## 🧠 Algoritmos implementados

### 🔹 Fatorial

O fatorial de um número inteiro não negativo `n` é definido por:

$$
n! = n \cdot (n-1) \cdot (n-2) \cdots 1
$$

com:

$$
0! = 1
$$

Foram implementadas duas versões:

- **Recursiva:** a função chama a si mesma, reduzindo o valor de `n` até atingir o caso base;
- **Iterativa:** utiliza um laço de repetição para realizar sucessivamente as multiplicações.

---

### 🔹 Fibonacci

A sequência de Fibonacci é definida pela relação:

$$
F(n) = F(n-1) + F(n-2)
$$

com os casos base:

$$
F(0) = 0
$$

$$
F(1) = 1
$$

Também foram implementadas duas versões:

- **Recursiva:** utiliza chamadas recursivas para calcular os dois termos anteriores;
- **Iterativa:** constrói os termos da sequência de forma sequencial utilizando um laço de repetição.

---

## 🧪 Testes experimentais

Para analisar o desempenho dos algoritmos, foram utilizados diferentes valores de entrada.

### Fatorial

```text
n = 5, 10, 50, 100, 500 e 1000
```

### Fibonacci

```text
n = 5, 10, 20, 30, 35 e 40
```

Para cada valor de `n`, cada algoritmo é executado **10 vezes**.

O tempo de cada execução é medido utilizando:

```python
time.perf_counter()
```

Os tempos obtidos são armazenados em listas e, posteriormente, é calculada a média:

```python
np.mean(tempos)
```

Dessa forma, para cada valor de entrada, o resultado utilizado na análise corresponde ao **tempo médio de 10 execuções**.

---

## ⚙️ Limite de recursão

Como o Fatorial recursivo é testado para valores de até `n = 1000`, o limite de recursão do Python foi aumentado para:

```python
import sys

sys.setrecursionlimit(2000)
```

Isso permite a execução do algoritmo recursivo para os valores utilizados no experimento.

---

## 📊 Organização dos dados

Como Fatorial e Fibonacci utilizam conjuntos diferentes de valores de `n`, os resultados são organizados em dois `DataFrames`.

### DataFrame do Fatorial

Contém:

- `n`;
- tempo médio do Fatorial recursivo;
- tempo médio do Fatorial iterativo.

### DataFrame do Fibonacci

Contém:

- `n`;
- tempo médio do Fibonacci recursivo;
- tempo médio do Fibonacci iterativo.

Os DataFrames são construídos utilizando a biblioteca **Pandas**.

---

## 📊 Complexidade assintótica

As complexidades de tempo analisadas são:

| Algoritmo | Complexidade |
| :--- | :---: |
| Fatorial iterativo | $O(n)$ |
| Fatorial recursivo | $O(n)$ |
| Fibonacci iterativo | $O(n)$ |
| Fibonacci recursivo | $O(2^n)$ |

Tanto o Fatorial recursivo quanto o iterativo realizam uma quantidade de operações proporcional ao valor de `n`.

O Fibonacci iterativo também percorre a sequência uma única vez, apresentando crescimento linear.

Já o Fibonacci recursivo realiza diversas chamadas repetidas, resultando em crescimento exponencial.

---

## 📈 Gráficos comparativos

Para visualizar os resultados experimentais, foram construídos dois gráficos utilizando **Matplotlib**:

- Desempenho do Fatorial;
- Desempenho do Fibonacci.

Em cada gráfico:

- o eixo **x** representa o valor de `n`;
- o eixo **y** representa o tempo médio de execução em segundos;
- uma linha representa a implementação **iterativa**;
- outra linha representa a implementação **recursiva**;
- marcadores indicam os valores efetivamente medidos.

Os limites do eixo vertical são definidos a partir dos menores e maiores tempos encontrados em cada conjunto de dados.

---

## 🔁 Recursão x Iteração

Na **recursão**, uma função chama a si mesma sucessivamente até atingir uma condição de parada, denominada **caso base**.

Na **iteração**, as repetições são realizadas por estruturas como `for` ou `while`.

Nos experimentos realizados, as implementações iterativas apresentaram menores tempos de execução.

No caso do Fatorial, ambas possuem a mesma complexidade assintótica:

$$
O(n)
$$

Entretanto, a implementação recursiva possui o custo adicional das sucessivas chamadas de função.

---

## 🐌 Por que o Fibonacci recursivo é tão lento?

O Fibonacci recursivo calcula:

$$
F(n) = F(n-1) + F(n-2)
$$

Assim, uma chamada gera outras duas chamadas recursivas.

Por exemplo:

```text
F(5)
├── F(4)
│   ├── F(3)
│   │   ├── F(2)
│   │   └── F(1)
│   └── F(2)
└── F(3)
    ├── F(2)
    └── F(1)
```

É possível perceber que alguns valores, como `F(3)` e `F(2)`, são calculados repetidamente.

Essa repetição gera uma grande quantidade de chamadas de função e faz com que o tempo de execução cresça exponencialmente:

$$
O(2^n)
$$

Nos testes realizados, essa diferença tornou-se especialmente evidente para valores maiores de `n`. Para `n = 40`, o Fibonacci recursivo apresentou tempo médio de execução da ordem de dezenas de segundos, enquanto a versão iterativa permaneceu muito mais rápida.

---

## 🛠️ Tecnologias utilizadas

- Python
- Google Colab / Jupyter Notebook
- NumPy
- Pandas
- Matplotlib
- módulo `time`
- módulo `sys`

---

## 📦 Bibliotecas utilizadas

```python
import time
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

---

## ▶️ Como executar

1. Faça o download ou clone este repositório;
2. Abra o arquivo `.ipynb` no **Google Colab** ou em outro ambiente compatível com Jupyter Notebook;
3. Execute as células na ordem apresentada;
4. Os algoritmos serão executados para os valores de `n` definidos no experimento;
5. Cada teste será repetido 10 vezes;
6. Os tempos médios serão armazenados nos DataFrames;
7. Ao final, serão apresentados os gráficos comparativos e a análise dos resultados.

> **Observação:** o Fibonacci recursivo para valores maiores de `n` pode levar um tempo considerável para concluir, devido à sua complexidade exponencial.

---

## ✅ Conclusão

Os resultados experimentais são compatíveis com o comportamento previsto pela análise assintótica.

Os algoritmos de Fatorial recursivo e iterativo possuem complexidade:

$$
O(n)
$$

assim como o Fibonacci iterativo:

$$
O(n)
$$

Já o Fibonacci recursivo apresenta crescimento exponencial:

$$
O(2^n)
$$

Experimentalmente, as versões iterativas apresentaram menores tempos de execução.

A diferença foi especialmente significativa no Fibonacci, pois a implementação recursiva recalcula diversas vezes os mesmos termos da sequência, gerando uma grande quantidade de chamadas recursivas.

O experimento demonstra, portanto, a relação entre a análise assintótica teórica e o comportamento observado durante a execução dos algoritmos.

---

## 👩‍💻 Autora

**Anna Beatriz Araújo Cardoso**

---

## 🎓 Instituição

**Pontifícia Universidade Católica de Goiás — PUC Goiás**

### Disciplina

**Projeto e Análise de Algoritmos**
