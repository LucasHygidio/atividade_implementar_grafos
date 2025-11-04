def criar_grafo():
    matriz = []
    vertices = []
    return matriz, vertices

def inserir_vertice(matriz, vertices, vertice): #refazer Lucas
    if vertice not in vertices:
        vertices.append(vertice)
        for i in range (len(vertices)):
            matriz[i].append(0)
        
        nova_linha = [0] * len(vertices)
        matriz.append(nova_linha)
            
matriz, vertices = criar_grafo()

# Adicionando vértices
inserir_vertice(matriz, vertices, "A")
inserir_vertice(matriz, vertices, "B")
inserir_vertice(matriz, vertices, "C")

# Exibindo resultados
print("Vértices do grafo:", vertices)
print("Matriz de adjacência:")
for linha in matriz:
    print(linha)


def inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=False): #Heloisa
    if (origem in vertices and destino in vertices):
        #Localizar indice:
        for i, linha in enumerate(matriz):
            if origem in matriz:
                j = linha.index(origem)
            if destino in matriz:
                j = linha.index(destino)
        return 'b'
    else:
        for vertice in vertices:
            inserir_vertice(matriz, vertices, vertice)
        inserir_aresta(matriz, vertices, origem, destino)
    """
    Adiciona uma aresta entre dois vértices.

    Passos:
    1. Garantir que 'origem' e 'destino' existam em 'vertices':
        - Se não existirem, chamar 'inserir_vertice' para adicioná-los.
    2. Localizar o índice da origem (i) e do destino (j).
    3. Marcar a conexão na matriz: matriz[i][j] = 1.
    4. Se nao_direcionado=True, também marcar a conexão inversa matriz[j][i] = 1.
    """
    pass


def remover_vertice(matriz, vertices, vertice): #Paola
    """
    Remove um vértice e todas as arestas associadas.

    Passos:
    1. Verificar se o vértice existe em 'vertices'.
    2. Caso exista:
        - Descobrir o índice correspondente (usando vertices.index(vertice)).
        - Remover a linha da matriz na posição desse índice.
        - Remover a coluna (mesmo índice) de todas as outras linhas.
        - Remover o vértice da lista 'vertices'.
    """
    
    if vertice in vertices:
        indice = vertices.index(vertice)
        matriz.pop(indice)
        
        for linha in matriz:
            linha.pop(indice)
            
        vertices.remove(vertice) 
        
        return f"Vertice {vertice} removido com sucesso!"
        #Precisa testar

def remover_aresta(matriz, vertices, origem, destino, nao_direcionado=False): #Heloisa
    """
    Remove uma aresta entre dois vértices.

    Passos:
    1. Verificar se ambos os vértices existem.
    2. Localizar os índices (i e j).
    3. Remover a aresta: matriz[i][j] = 0.
    4. Se nao_direcionado=True, também remover a inversa: matriz[j][i] = 0.
    """
    pass


def existe_aresta(matriz, vertices, origem, destino): #Lucas
    """
    Verifica se existe uma aresta direta entre dois vértices.

    Passos:
    1. Verificar se ambos os vértices existem em 'vertices'.
    2. Obter os índices (i, j).
    3. Retornar True se matriz[i][j] == 1, caso contrário False.
    """
    pass


def vizinhos(matriz, vertices, vertice): #paola
    """
    Retorna a lista de vizinhos (vértices alcançáveis a partir de 'vertice').

    Passos:
    1. Verificar se 'vertice' existe em 'vertices'.
    2. Obter o índice 'i' correspondente.
    3. Criar uma lista de vizinhos vazia
    4. Para cada item da linha matriz[i], verificar se == 1
        - Adicionar o vértice correspondente na lista de vizinhos
    5. Retornar essa lista.
    """
    if vertice in vertices:
        indice = vertices.index(vertice)
        
        vizinhos = []
        
        for i in range(len(matriz[indice])):
            if matriz[indice][i] == 1:
                vizinhos.append(vertice[i])
            
        return vizinhos
        #Precisa testar

def grau_vertices(matriz, vertices):#helo
    """
    Calcula o grau de entrada, saída e total de cada vértice.

    Passos:
    1. Criar um dicionário vazio 'graus'.
    2. Para cada vértice i:
        - Se o grafo for direcionado:
            - Grau de saída: somar os valores da linha i.
            - Grau de entrada: somar os valores da coluna i.
            - Grau total = entrada + saída.
        - Se não:
            - calcular apenas o grau de saida ou entrada
    3. Armazenar no dicionário no formato:
        graus[vértice] = {"saida": x, "entrada": y, "total": z} ou graus[vértice] = x.
    4. Retornar 'graus'.
    """
    pass


def percurso_valido(matriz, vertices, caminho):#lucas
    """
    Verifica se um percurso (sequência de vértices) é possível no grafo.

    Passos:
    1. Percorrer a lista 'caminho' de forma sequencial (de 0 até len-2).
    2. Para cada par consecutivo (u, v):
        - Verificar se existe_aresta(matriz, vertices, u, v) é True.
        - Se alguma não existir, retornar False.
    3. Se todas existirem, retornar True.
    """
    pass


def listar_vizinhos(matriz, vertices, vertice):#paola
    """
    Exibe (ou retorna) os vizinhos de um vértice.

    Passos:
    1. Verificar se o vértice existe.
    2. Chamar a função vizinhos() para obter a lista.
    3. Exibir a lista formatada (ex: print(f"Vizinhos de {v}: {lista}")).
    """
    pass


def exibir_grafo(matriz, vertices):#heloisa
    """
    Exibe o grafo em formato de matriz de adjacência.

    Passos:
    1. Exibir cabeçalho com o nome dos vértices.
    2. Para cada linha i:
        - Mostrar o nome do vértice.
        - Mostrar os valores da linha (0 ou 1) separados por espaço.
    """
    pass


def main(): #paola

    pass


if __name__ == "__main__":
    main()
