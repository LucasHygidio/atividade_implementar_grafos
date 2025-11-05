def criar_grafo():
    matriz = []
    vertices = []
    return matriz, vertices

def inserir_vertice(matriz, vertices, vertice):
    if vertice in vertices:
        return 
    vertices.append(vertice)
    for linha in matriz:
        linha.append(0)
    nova_linha = [0] * len(vertices)
    matriz.append(nova_linha)
matriz, vertices = criar_grafo()

#teste
inserir_vertice(matriz, vertices, "A")
inserir_vertice(matriz, vertices, "B")
inserir_vertice(matriz, vertices, "C")


print("Vértices do grafo:", vertices)
print("Matriz de adjacência:")
for linha in matriz:
    print(linha)


def inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=False): #Heloisa
    if (origem in vertices and destino in vertices):
        i = vertices.index(origem)
        j = vertices.index(destino)
        matriz[i][j] = 1
        
        if nao_direcionado:
            matriz[i][j] = 1
    else:
        for vertice in vertices:
            inserir_vertice(matriz, vertices, vertice)
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

matriz1, vertices1 = criar_grafo()
inserir_vertice(matriz1, vertices1, "b")
inserir_vertice(matriz1, vertices1, "c")
inserir_aresta(matriz1, vertices1, 'b', 'c')
for linha in matriz1:
    print(linha)

def remover_vertice(matriz, vertices, vertice): #Paola
    
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

    if origem in vertices and destino in vertices:
        i = vertices.index(origem)
        j = vertices.index(destino)
        if matriz[i][j] == 1:
            return True
        else:
            return False
    else: 
        False


def vizinhos(matriz, vertices, vertice): #paola

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


def percurso_valido(matriz, vertices, caminho:list ):#lucas
    """
    Verifica se um percurso (sequência de vértices) é possível no grafo.

    Passos:
    1. Percorrer a lista 'caminho' de forma sequencial (de 0 até len-2).
    2. Para cada par consecutivo (u, v):
        - Verificar se existe_aresta(matriz, vertices, u, v) é True.
        - Se alguma não existir, retornar False.
    3. Se todas existirem, retornar True.
    """
    
    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i + 1]
        
        if not existe_aresta(matriz, vertices, origem, destino):
            return False
    
    return True
            
        



def listar_vizinhos(matriz, vertices, vertice):#paola
    """
    Exibe (ou retorna) os vizinhos de um vértice.

    Passos:
    1. Verificar se o vértice existe.
    2. Chamar a função vizinhos() para obter a lista.
    3. Exibir a lista formatada (ex: print(f"Vizinhos de {v}: {lista}")).
    """
    if vertice in vertices:
        lista = vizinhos(matriz, vertices, vertice)
    
        print(f"Vizinhos de {vertice}: {lista}")
        #Precisa testar


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

    continuar = True
    
    while continuar:
        print("""
                1 - Mostrar o Grafo
                2 - Inserir vertice
                3 - Inserir aresta
                4 - Remover vértice
                5 - Remover aresta
                6 - Verificar se a aresta existe
                7 - Listar todos os vizinhos 
                8 - Grau de um vertice
                9 - Percurso valido
                10 - Lista vizinho de um vertice
                0 - Sair
              """)
        
        opcao = input(str("\nEscolha uma opção: "))
        
        match opcao:
            case "1":
                print("Mostrar o Grafo\n")
                exibir_grafo(g1)
                
                
            case "2":
                print("Inserir vertice\n")
                vertice = input(str("Digite o valor do Vertice: "))
                
                inserir_vertice(g1, vertice)
                
                
            case "3":
                print("Inserir aresta\n")
                aresta_origem = input(str("Digite a ORIGEM da aresta: "))
                aresta_destino = input(str("Digite o DESTINO da aresta: "))
                
                inserir_aresta(g1, aresta_origem, aresta_destino)
                
                
            case "4":
                print("Remover vertice")
                vertice_removido = input(str("Digite o vertice que deseja remover: "))
                
                remover_vertice(g1, vertice_removido)
            
            
            case "5":
                print("Remover aresta")
                #remover_aresta()
            
            
            case "6":
                print("Verificar se a aresta existe")
                #existe_aresta()
                
                
            case "7":
                print("Listar todos os vizinhos")
                listar_vizinhos(matriz, vertice, vertices)
                
                
            case "0":
                print("Fim!")
                continuar = False   
                
                """
                1 - Mostrar o Grafo
                2 - Inserir vertice
                3 - Inserir aresta
                4 - Remover vértice
                5 - Remover aresta
                6 - Verificar se a aresta existe
                7 - Listar todos os vizinhos 
                8 - Grau de um vertice
                9 - Percurso valido
                10 - Lista vizinho de um vertice
                0 - Sair
              """ 


if __name__ == "__main__":
    g1 = criar_grafo()
    main()
