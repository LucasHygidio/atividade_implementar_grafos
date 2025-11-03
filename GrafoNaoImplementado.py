def criar_grafo() -> dict:
    grafo = {}
    return grafo


def inserir_vertice(grafo, vertice) -> None:
    if (vertice in grafo.keys()):
        print("Vertice ja existente")
    else:
        grafo[vertice] = []


def inserir_aresta(grafo, origem, destino, nao_direcionado=False) -> None:
    if origem not in grafo.keys():
        inserir_vertice(grafo, origem)
    if destino not in grafo.keys():
        inserir_vertice(grafo, destino)
        
    grafo[origem].append(destino)
    
    if nao_direcionado:
        grafo[destino].append(origem)


def vizinhos(grafo, vertice):
    if vertice in grafo.keys():
        return grafo[vertice]
    
    else:
        print(f"Vértice '{vertice}' não encontrado")


def listar_vizinhos(grafo, vertice):
    if vertice in grafo.keys():
        lista_vizinhos = list
        lista_vizinhos.append(vizinhos(grafo, vertice))
        return listar_vizinhos
    
    else:
        print(f"Vértice '{vertice}' não encontrado")
        return "Vertice não encontrado no grafo"
    
    
def exibir_grafo(grafo):
    for chave in grafo:
        print(f"{chave} -> {vizinhos(grafo, chave)}")


def remover_aresta(grafo, origem, destino, nao_direcionado=False):
    if (origem not in grafo.keys()):
        return "Origem não existente no grafo"
    
    if destino in grafo[origem]:
        if nao_direcionado:
            grafo[destino].remove(origem)
        grafo[origem].remove(destino)


def remover_vertice(grafo, vertice, nao_direcionado=True):
    if vertice not in grafo.keys():
        return "Vertice não encontrado"
    
    for chave in grafo:
        if vertice in grafo[chave]:
            grafo[chave].remove(vertice)
        
    del grafo[vertice]


def existe_aresta(grafo, origem, destino):
    if (origem in grafo.keys() and destino in grafo[origem]):
        return True
    else:
        return False


def grau_vertices(grafo):
    grau_vertice = {}
    
    grau_vertice = {
        "in" : "",
        "out": "",
        "total": listar_vizinhos() # + total entrada + saida
    }
    
    #percorrer a matriz de grafos e verificar quais as arestas estão presentes
    
    return grau_vertice

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


def percurso_valido(grafo, caminho):
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