class Grafo:
    def __init__(self, direcionado = False):
        self.grafo = {}
        if self.grafo.keys() == [""]:
            self.direcionado= direcionado


    def inserir_vertice(self, vertice:str):
        if vertice not in self.grafo.keys():
            self.grafo[vertice] = []
        else:
            print("Vertice ja existente no grafo")
        return self.grafo


    def inserir_aresta(self, origem:str, destino:str):
        if origem not in self.grafo.keys():
            self.inserir_vertice(self.grafo, origem)
        if destino not in self.grafo.keys():
            self.inserir_vertice(self.grafo, destino)
        
        if self.direcionado == True:
            self.grafo[origem].append(destino)
            
        else:
            self.grafo[origem].append(destino)
            self.grafo[destino].append(origem)    

    def vizinhos(self, vertice:str):
        #Lucas
        """
        Retorna a lista de vizinhos de 'vertice'.
        Passos:
        1. Se 'vertice' estiver em grafo, retornar grafo[vertice] (lista).
        2. Se não existir, retornar lista vazia ou sinalizar erro.
        """
        if vertice in self.grafo.keys():
            pass

    def listar_vizinhos(self, vertice):
        """
        Função semântica: imprimir/retornar os vizinhos de 'vertice'.
        Passos:
        1. Obter lista = vizinhos(grafo, vertice)
        2. Retornar/imprimir essa lista (ou informar que o vértice não existe)
        """
        pass

    def exibir_grafo(self):
        """
        Exibe o grafo em forma legível (lista de adjacência).
        Passos:
        1. Para cada vertice em ordem
            - imprimir: vertice -> vizinhos
        """
        pass

    def remover_aresta(self, origem, destino):
        """
        Remove a aresta entre origem e destino.
        Passos:
        1. Verificar se 'origem' existe; se não, terminar.
        2. Se destino estiver em grafo[origem], remover essa ocorrência.
        3. Se for não direcionado, também:
            - verificar se 'destino' existe e remover 'origem' de grafo[destino] se presente.
        """
        pass


    def remover_vertice(self, vertice):
        """
        Remove um vértice e todas as arestas que o tocam.
        Passos:
        1. Verificar se 'vertice' existe em grafo; se não, terminar.
        2. Para cada outro vertice no grafo:
            - se 'vertice' estiver na lista de vizinhos, remover essa aresta.
        3. Remover o vertice do grafo
        4. Opcional: retornar confirmação/erro.
        """
        pass


    def existe_aresta(self, origem, destino):
        """
        Verifica se existe aresta direta origem -> destino.
        Passos:
        1. Verificar se 'origem' é chave no grafo.
        2. Retornar True se 'destino' estiver em grafo[origem], caso contrário False.
        """
        pass

    def grau_vertices(self):
        """
        Calcula e retorna o grau (out, in, total) de cada vértice.
        Passos:
        1. Inicializar um dict de graus vazia
        2. Para cada vertice, colocar no dict uma estrutura com in, out e total zerado
        3. Para cada u em grafo:
            - out_degree[u] = tamanho de vizinhos
            - para cada v em grafo:
                - verificar se u está na lista de vizinho de v,
                - caso esteja, adicionar +1 para o grau de entrada de u
        4. Calcular o grau total somando entrada + saida
        5. Retornar uma estrutura contendo out,in,total por vértice (ex: dict de tuplas).
        """
        pass


    def percurso_valido(self, caminho):
        """
        Verifica se uma sequência específica de vértices (caminho) é válida:
        i.e., se existem arestas consecutivas entre os nós do caminho.
        Passos:
        1. Se caminho tiver tamanho < 2, retornar True (trivial).
        2. Para i de 0 até len(caminho)-2:
            - origem = caminho[i], destino = caminho[i+1]
            - se não existe_aresta(grafo, origem, destino): retornar False
        3. Se todas as arestas existirem, retornar True.
        """
        pass



def main():
    """
    Crie um menu onde seja possível escolher qual ação deseja realizar
    ex:
        1 - Mostrar o Grafo
        2 - inserir vertice
        3 - inserir aresta
        4 - remover vértice.
        ....
    """
    pass


if __name__ == "__main__":
    main()
