def criar_grafo():#Lucas
    """
    Cria e retorna uma estrutura de grafo com lista de arestas e lista de vértices.

    Passos:
    1. Criar uma lista vazia chamada 'vertices'.
    2. Criar uma lista vazia chamada 'arestas', onde cada elemento será uma lista de tamanho 2 (origem, destino)
    3. Retornar vertices e arestas
    """
    pass


def inserir_vertice(vertices, vertice):#heloisa
    """
    Adiciona um novo vértice no grafo.

    Passos:
    1. Verificar se o vértice já existe em 'vertices'.
    2. Se não existir, adicionar à lista 'vertices'.
    """
    pass

def inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=False):#Paola
    """
    Adiciona uma aresta entre dois vértices.

    Passos:
    1. Garantir que 'origem' e 'destino' existam em 'vertices'.
       - Se não existirem, chamar 'inserir_vertice' para adicioná-los.
    2. Adicionar uma lista [origem, destino] na lista 'arestas'.
    3. Se nao_direcionado=True, adicionar também [destino, origem].
    """
    pass

def remover_aresta(arestas, origem, destino, nao_direcionado=False):#Lucas
    """
    Remove uma aresta entre dois vértices.

    Passos:
    1. Percorrer a lista de Arestas procurando [origem, destino]
    2. Se encontrar, remover
    3. Se nao_direcionado=True, também procurar por [destino, origem]
    """
    pass

def remover_vertice(vertices, arestas, vertice):#Heloisa
    """
    Remove um vértice e todas as arestas conectadas a ele.

    Passos:
    1. Verificar se o vértice existe na lista de vertices.
    2. Caso encontrado, remover o vértice da lista 'vertices'.
    3. Percorrer a lista de 'arestas' e remover todas onde o vértice aparece
       como origem ou destino.
    """
    pass

def existe_aresta(arestas, origem, destino):#Paola
    """
    Verifica se existe uma aresta entre origem e destino.

    Passos:
    1. Percorrer a lista de aresta procurando [origem, destino]
    2. Retornar True se encontrar
    3. Caso não encontre na lista, retornar False no final.
    """
    pass


def vizinhos(vertices, arestas, vertice):#Lucas
    """
    Retorna a lista de vizinhos (vértices alcançáveis a partir de 'vertice').

    Passos:
    1. Criar uma lista vazia chamada 'vizinhos'.
    2. Percorrer todas as arestas [origem, destino].
    3. Se origem == vertice, adicionar destino na lista de vizinhos.
    4. Retornar a lista final.
    """
    pass


def grau_vertices(vertices, arestas):#heloisa
    """
    Calcula o grau de entrada, saída e total de cada vértice.

    Passos:
    1. Criar um dicionário vazio 'graus'.
    2. Percorrer todas as arestas [origem, destino]:
        I. Se o grafo for não direcionado:
            - incrementar grau analisando apenas se origem ou destino equivale ao vértice analisado
        II. Se o grafo for direcionado
            - Se o vértice for origem Incrementar grau de saída do vértice origem
            - Se o vértice for destino incrementar grau de entrada do vértice destino.
            - Calcular o grau total (entrada + saída).
    4. Retornar o dicionário 'graus' para cada vértice.
    """
    pass


def percurso_valido(arestas, caminho):#Paola
    """
    Verifica se um percurso é possível (seguindo as arestas na ordem dada).

    Passos:
    1. Percorrer o caminho de 0 até len(caminho) - 2.
    2. Para cada par consecutivo (u, v):
        - Verificar se (u, v) existe na lista de 'arestas' (funcao existe_aresta).
        - Se alguma não existir, retornar False.
    3. Se todas existirem, retornar True.
    """
    pass


def listar_vizinhos(vertices, arestas, vertice):#Lucas
    """
    Exibe os vizinhos de um vértice.

    Passos:
    1. Chamar a função vizinhos() para obter a lista.
    2. Exibir a lista formatada.
    """
    pass


def exibir_grafo(vertices, arestas):#Heloisa
    """
    Exibe todas as arestas do grafo.

    Passos:
    1. Exibir a lista de vértices.
    2. Exibir todas as arestas no formato (origem -> destino).
    """
    pass


def main():#Paola
    pass


if __name__ == "__main__":
    main()
