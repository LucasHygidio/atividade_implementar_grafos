def criar_grafo():#Lucas
    vertices = []
    arestas = []
    return vertices, arestas

def inserir_vertice(vertices, vertice):#Lucas
    if vertice not in vertices:
        vertices.append(vertice)

def inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=False):#Lucas
    if origem not in vertices:
        inserir_vertice(vertices, origem)
    if destino not in vertices:
        inserir_vertice(vertices, destino)
    if [origem, destino] not in arestas:
        arestas.append([origem, destino])
    if nao_direcionado and [destino, origem] not in arestas:
        arestas.append([destino, origem])

def remover_aresta(arestas, origem, destino, nao_direcionado=False):#Lucas
    if [origem, destino] in arestas:
        arestas.remove([origem, destino])

    if nao_direcionado and [destino, origem] in arestas:
        arestas.remove([destino, origem])
            
def remover_vertice(vertices, arestas, vertice):#Lucas
    if vertice in vertices:
        novas_arestas = []
        for a in arestas:
            if vertice not in a:
                novas_arestas.append(a)
        arestas[:] = novas_arestas
        vertices.remove(vertice)

def existe_aresta(arestas, origem, destino):#Lucas
    if [origem, destino] in arestas:
        return True
    return False


def vizinhos(vertices, arestas, vertice):#Lucas
    vizinhos = []
    if vertice in vertices:
        for i in range (len(arestas)):
            if arestas[i][0] == vertice:
                vizinhos.append(arestas[i][1])
    return vizinhos


def grau_vertices(vertices, arestas, nao_direcionado = False):#heloisa
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
