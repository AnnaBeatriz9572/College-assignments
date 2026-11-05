#Lista encadeada
class No:
    def __init__(self, valor):  # para armazenar o valor dentro do objeto
        self.valor = valor
        self.proximo = None  # incialmente não aponta para outro nó


class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def inserir_inicio(self, valor):
        # criar um nó
        novo_no = No(valor)  # por enquanto criamos apenas um nó que está separado do resto da lista
        # conectar o novo nó ao início atual
        novo_no.proximo = self.inicio
        # atualizar o início da lista
        self.inicio = novo_no

    def inserir_final(self, valor):
        # criamos o novo nó
        novo_no = No(valor)
        # se for o primeiro da lista nós modificamos apenas o atributo do objeto
        if self.inicio is None:
            self.inicio = novo_no
            return
        # criamos uma varíavel que aponta para o endereço atual
        atual = self.inicio
        # conectar o último nó ao novo nó
        while atual.proximo is not None:
            atual = atual.proximo

        atual.proximo = novo_no

    def remover_no(self, valor):
        if self.inicio is None:
            return

        # caso o nó esteja no início da lista
        if self.inicio.valor == valor:
            self.inicio = self.inicio.proximo
            return

        # remove do meio ou do final em uma lista
        anterior = self.inicio
        atual = self.inicio.proximo

        while atual is not None and atual.valor != valor:
            anterior = atual
            atual = atual.proximo

        if atual is None:
            return

        anterior.proximo = atual.proximo

    def imprimir_lista(self):
        atual = self.inicio
        valores = []
        
        while atual is not None:
            valores.append(atual.valor)
            atual = atual.proximo
            
        print(valores)

    def busca_lista(self, valor):
        atual = self.inicio

        while atual is not None and atual.valor != valor:
            atual = atual.proximo

        if atual is None:
            return False
        else:
            return True

    def tamanho_lista(self):
        atual = self.inicio
        contador = 0

        while atual is not None:
            contador += 1
            atual = atual.proximo

        return contador
    def bubble_sort(self, visualizar=False):
        if not self.inicio or not self.inicio.proximo:
            return

        passou_limite = None
        trocou = True

        while trocou:
            trocou = False
            atual = self.inicio

            while atual.proximo != passou_limite:
                if atual.valor > atual.proximo.valor:
                    atual.valor, atual.proximo.valor = atual.proximo.valor, atual.valor
                    trocou = True
                    # Se visualizar for True, imprime a lista na tela logo após a troca
                    if visualizar:
                        self.imprimir_lista()
                
                atual = atual.proximo
            
            passou_limite = atual
            
#Testes
print("TESTE 1: Lista com Valores Aleatórios")
lista_aleatoria = ListaEncadeada()
valores_1 = [42, 7, 19, 3, 55, 22, 11]
for v in valores_1:
    lista_aleatoria.inserir_final(v)

print("Lista original:")
lista_aleatoria.imprimir_lista()

print("Realizando trocas (Passo a passo):")
lista_aleatoria.bubble_sort(visualizar=True)

print("Lista ordenada (Bubble Sort):")
lista_aleatoria.imprimir_lista()
print(f"Tamanho da lista: {lista_aleatoria.tamanho_lista()}\n")


print("TESTE 2: Lista Quase Ordenada")
lista_quase = ListaEncadeada()
valores_2 = [2, 3, 5, 4, 6, 8, 7, 10]
for v in valores_2:
    lista_quase.inserir_final(v)

print("Lista original:")
lista_quase.imprimir_lista()

lista_quase.bubble_sort()

print("Lista ordenada (Bubble Sort):")
lista_quase.imprimir_lista()
print(f"Tamanho da lista: {lista_quase.tamanho_lista()}\n")


print("TESTE 3: Lista em Ordem Inversa")
lista_inversa = ListaEncadeada()
valores_3 = [50, 40, 30, 20, 10, 5]
for v in valores_3:
    lista_inversa.inserir_final(v)

print("Lista original:")
lista_inversa.imprimir_lista()

lista_inversa.bubble_sort()

print("Lista ordenada (Bubble Sort):")
lista_inversa.imprimir_lista()
print(f"Tamanho da lista: {lista_inversa.tamanho_lista()}")
