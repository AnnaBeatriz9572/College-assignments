# Resolvedor de Sudoku 🧩

Olá, pessoal! 👋

Este projeto surgiu a partir de um desafio proposto pelo meu professor. Durante uma aula, estávamos assistindo a um vídeo do canal **Computerphile**, quando ele sugeriu que tentássemos desenvolver nosso próprio resolvedor de Sudoku e explorar possíveis melhorias ao longo do processo.

O desafio despertou minha curiosidade, então decidi colocá-lo em prática! Desenvolvi o projeto em **Python**, utilizando um **Jupyter Notebook**, com foco na implementação da lógica de resolução e na criação de verificações para garantir que a matriz inicial respeite as regras do Sudoku.

## O que o programa faz?

O programa resolve quebra-cabeças tradicionais de **Sudoku 9×9** utilizando a técnica de **backtracking recursivo** (retrocesso).

O algoritmo testa os números possíveis em cada posição vazia, explora as consequências de cada escolha e retorna às etapas anteriores sempre que encontra um caminho que não leva a uma solução.

A seguir, explico como cada parte funciona!

## Etapa 1 — Representação do Sudoku

O Sudoku é armazenado em uma variável chamada `grid`, que consiste em uma lista contendo outras nove listas.

Cada lista interna representa uma linha, e cada valor corresponde a uma célula da matriz:

- Números de `1` a `9` representam os valores já fornecidos no Sudoku.
- O número `0` representa uma célula vazia que precisa ser preenchida.

Ao longo do código, `y` representa o índice da linha, `x` representa o índice da coluna e `n` corresponde ao número que está sendo testado.

## Etapa 2 — Verificação das dimensões da matriz

Antes de iniciar a busca por uma solução, a função `check_matrix()` verifica se o Sudoku possui:

- Exatamente nove linhas.
- Exatamente nove valores em cada linha.

Essa verificação garante que o algoritmo receba uma matriz com as dimensões esperadas antes de acessar suas células.

## Etapa 3 — Verificação dos números possíveis

A função `possible(y, x, n)` verifica se o número `n` pode ser inserido em uma determinada célula vazia.

Para isso, são realizadas três verificações:

1. **Linha:** o número não pode estar presente na mesma linha.
2. **Coluna:** o número não pode estar presente na mesma coluna.
3. **Bloco 3×3:** o número não pode estar presente no mesmo bloco.

Para identificar onde começa o bloco 3×3 correspondente à célula analisada, utilizamos:

```python
y0 = (y // 3) * 3
x0 = (x // 3) * 3
```

Como os índices começam em zero, esses cálculos determinam a linha e a coluna iniciais do bloco ao qual a célula pertence.

Se o número respeitar as três condições, a função retorna `True`. Caso contrário, retorna `False`.

## Etapa 4 — Validação dos números iniciais

Verificar os novos números não é suficiente. Também precisamos garantir que os valores já presentes no Sudoku respeitem suas regras!

A função `check_sudoku()` percorre todas as células e verifica se cada valor é um número inteiro entre `0` e `9`.

Para cada célula preenchida, a função:

1. Armazena temporariamente o número original.
2. Substitui esse número por `0`.
3. Chama a função `possible()` para verificar possíveis conflitos.
4. Restaura o número original antes de continuar ou retornar `False`.

A substituição temporária é importante porque, caso contrário, a função `possible()` encontraria o próprio número na célula analisada e o identificaria incorretamente como uma repetição.

Dessa forma, a validação mantém os valores originais do Sudoku, inclusive quando identifica uma matriz inválida.

## Etapa 5 — Busca por uma solução

A função `solve()` começa executando as funções de validação.

Se a matriz for inválida, o programa exibe uma mensagem de erro. Caso contrário, percorre a matriz até encontrar uma célula vazia.

Ao encontrar essa célula, o algoritmo testa os números de `1` a `9`.

Sempre que a função `possible()` identifica um número válido, o algoritmo o insere na matriz e realiza uma nova chamada à função `solve()`.

Essa chamada recursiva continua a busca considerando o número que acabou de ser inserido.

## Etapa 6 — Retrocesso e tentativa de novos caminhos

Um número pode ser válido para uma determinada célula, mas ainda assim levar a uma situação sem solução nas próximas etapas.

Quando uma chamada recursiva termina, a seguinte instrução remove o número que estava sendo testado:

```python
grid[y][x] = 0
```

Assim, o algoritmo pode testar o próximo candidato.

Esse processo é chamado de **backtracking**: realizar uma escolha, explorar suas possibilidades, desfazer a escolha e tentar outro caminho.

## Etapa 7 — Exibição dos resultados

Quando o algoritmo encontra uma matriz sem células vazias, ele exibe o Sudoku completo utilizando o NumPy:

```python
print(np.matrix(grid))
```

A busca continua após encontrar uma solução. Portanto, caso o Sudoku possua múltiplas soluções, o programa poderá apresentar diferentes matrizes completas.

Ao finalizar a execução:

- A variável `grid` retorna ao seu estado original.
- A função `solve()` retorna `None`.
- Se o Sudoku for válido, mas não possuir solução, nenhuma matriz será exibida.

## Como executar o projeto?

Para executar o resolvedor, você precisará de **Python 3**, **NumPy** e **Jupyter Notebook**.

Primeiro, instale as dependências:

```bash
python -m pip install numpy notebook
```

Em seguida, abra o notebook:

```bash
jupyter notebook resolvedor_sudoku.ipynb
```

Execute a célula de importação, defina o Sudoku na variável `grid` e execute as células que contêm as funções.

Depois, basta chamar:

```python
solve()
```

Para testar outro Sudoku, atribua uma nova matriz à variável `grid` e execute novamente a função `solve()`.

## O que estou aprendendo com este projeto?

Este projeto foi uma oportunidade de explorar, na prática, conceitos importantes de programação, como **recursividade, backtracking, manipulação de matrizes e validação de entradas**, a partir de um desafio discutido em sala de aula.

Além disso, pude compreender melhor a importância de validar os dados antes de executar um algoritmo e os cuidados necessários ao modificar temporariamente valores durante uma verificação, garantindo que sejam restaurados corretamente.

Foi uma experiência interessante para aprofundar meus conhecimentos em lógica de programação e resolução de problemas!

**Obrigada por conhecer o projeto!** Fique à vontade para testar o notebook com seus próprios desafios de Sudoku. 🙂
