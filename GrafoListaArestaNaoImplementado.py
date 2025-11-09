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
    graus = {}
    for v in vertices:
        graus[v] = {"saida": 0, "entrada": 0}

    for aresta in arestas:
        origem = aresta[0]
        destino = aresta[1]
        
        if origem in graus:
            graus[origem]["saida"] += 1
            
        if destino in graus:
            graus[destino]["entrada"] += 1
            
    for v in graus:
        graus[v]["total"] = graus[v]["saida"] + graus[v]["entrada"]
        
    return graus
    

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
    for i in range(len(caminho) - 2):
        u = caminho[i]
        v = caminho[i + 1]
        
        if not existe_aresta(arestas, u, v):
            return False 

    return True  


def listar_vizinhos(vertices, arestas, vertice):#Paola
    """
    Exibe os vizinhos de um vértice.

    Passos:
    1. Chamar a função vizinhos() para obter a lista.
    2. Exibir a lista formatada.
    """
    lista = vizinhos(vertices, arestas, vertice)
    
    if lista:
        print(f"Vizinhos de {vertice}: {lista}")
    else:
        print(f"O vértice '{vertice}' não possui vizinhos ou não existe.")


def exibir_grafo(vertices, arestas):#Heloisa
    """
    Exibe todas as arestas do grafo.

    Passos:
    1. Exibir a lista de vértices.
    2. Exibir todas as arestas no formato (origem -> destino).
    """
    print(f"Vértices: {vertices}")
    
    print("Arestas:")
    
    if not arestas:
        print("  (Grafo vazio, sem arestas)")
    else:
        for aresta in arestas:
            print(f"  {aresta[0]} -> {aresta[1]}")


def main():#Paola
    continuar = True
    nao_direcionado = False
    while True:
        resposta = input("O grafo é direcionado ? ").lower().strip()

        if resposta in ["s", "n"]:
            break 
        else:
            print("Erro: Resposta inválida. Por favor, digite apenas 's' ou 'n'.")
    
    if resposta == "n":
        nao_direcionado = True

    while continuar:
        print("""
                1 - Exibir o Grafo
                2 - Inserir vertice
                3 - Inserir aresta
                4 - Remover aresta
                5 - Remover vertice
                6 - Existe aresta
                7 - Grau de todos os vertices
                8 - Percurso valido
                9 - Listar todos os vizinhos 
                0 - Sair
              """)
        
        opcao = input(str("\nEscolha uma opção: "))
        
        match opcao:
            case "1":
               exibir_grafo(vertices, arestas)
           
           
            case "2":
                v = input(str("Digite o valor do vertice: "))
                inserir_vertice(vertices, v)
                
                
            case "3":
                o = input(str("Digite a ORIGEM da aresta: "))
                d = input(str("Digite o DESTINO da aresta: "))
                
                inserir_aresta(vertices, arestas, o, d, nao_direcionado)
            
            
            case "4":
                o = input(str("Digite a ORIGEM da aresta a ser removida: "))
                d = input(str("Digite o DESTINO da aresta a ser removida: "))
                
                remover_aresta(arestas, o, d, nao_direcionado)
                
            
            case "5":
                v = input(str("Digite o VERTICE a ser removido: "))
                remover_vertice(vertices, arestas, v)
                
                
            case "6":
                o = input(str("Digite a ORIGEM da aresta: "))
                d = input(str("Digite o DESTINO da aresta: "))
                
                aresta = existe_aresta(arestas, o, d)
                
                if aresta:
                    print(f"A aresta [{o}, {d}] existe no grafo")
                else:
                    print(f"A aresta [{o}, {d}] não existe no grafo!")
                
                
            case "7":
                grau = grau_vertices(vertices, arestas, nao_direcionado)
                print(f"{grau}\n")
            
            
            case "8":
                c = input("Digite o caminho a ser percorrido: ")
                cam = c.split(', ')
                
                percurso = percurso_valido(arestas, cam)
                
                if percurso:
                   print("O percurso é valido")
                   
                else:
                    print("O percurso não é possivel")
                
               
            case "9":
                v = input(str("Digite o vartice: "))
                
                listar_vizinhos(vertices, arestas, v)
            
            
            case "0":
                print("Fim!")
                continuar = False   


if __name__ == "__main__":
    vertices, arestas = criar_grafo()
    main()
