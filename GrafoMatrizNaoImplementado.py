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
    """
    Adiciona uma aresta entre dois vértices.

    Passos:
    1. Garantir que 'origem' e 'destino' existam em 'vertices':
       - Se não existirem, chamar 'inserir_vertice' para adicioná-los.
    2. Localizar o índice da origem (i) e do destino (j).
    3. Marcar a conexão na matriz: matriz[i][j] = 1.
    4. Se nao_direcionado=True, também marcar a conexão inversa matriz[j][i] = 1.
    """
    
    if origem not in vertices:
        print(f"Vértice '{origem}' não existia. Adicionando...")
        inserir_vertice(matriz, vertices, origem)
        
    if destino not in vertices:
        print(f"Vértice '{destino}' não existia. Adicionando...")
        inserir_vertice(matriz, vertices, destino)
        
    i = vertices.index(origem)
    j = vertices.index(destino)
    
    matriz[i][j] = 1
    
    if nao_direcionado:
        matriz[j][i] = 1
    

matriz1, vertices1 = criar_grafo()
# inserir_vertice(matriz1, vertices1, "b")
# inserir_vertice(matriz1, vertices1, "c")
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
    
    if origem not in vertices or destino not in vertices:
        print(f"Erro:Um ou os dois vertives ({origem}, {destino}) não existem no grafo.")
        return 

    i = vertices.index(origem)
    j = vertices.index(destino)
    
    matriz[i][j] = 0
    
    if nao_direcionado:
        matriz[j][i] = 0


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
        
        vizinho = []
        
        for i in range(len(matriz[indice])):
            if matriz[indice][i] == 1:
                vizinho.append(vertices[i])
            
        return vizinho


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
    graus = {}
    num_vertices = len(vertices)
    
    for i, vertice in enumerate(vertices):
        
        grau_saida = sum(matriz[i])
        
        grau_entrada = 0
        for j in range(num_vertices):
            grau_entrada += matriz[j][i]
            
        grau_total = grau_saida + grau_entrada
        
        graus[vertice] = {
            "saida": grau_saida,
            "entrada": grau_entrada,
            "total": grau_total
        }
        
    return graus


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
    print("  ", end=" ") 
    for v in vertices:
        print(v, end=" ")
    print() 
    for i, linha in enumerate(matriz):
        print(f"{vertices[i]} ", end=" ")
        
        print(" ".join(str(valor) for valor in linha))


def main(): #paola

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
                1 - Mostrar o Grafo
                2 - Inserir vertice
                3 - Inserir aresta
                4 - Remover vértice
                5 - Remover aresta
                6 - Verificar se a aresta existe
                7 - Grau de um vertice
                8 - Percurso valido
                9 - Listar todos os vizinhos de todos os vertices
                0 - Sair
              """)
        
        opcao = input(str("\nEscolha uma opção: "))
        
        match opcao:
            case "1":
                print("Mostrar o Grafo\n")
                exibir_grafo(matriz, vertices)
                
                
            case "2":
                print("Inserir vertice\n")
                v = input(str("Digite o valor do Vertice: "))
                
                inserir_vertice(matriz, vertices, v)
                
                
            case "3":
                print("Inserir aresta\n")
                o = input(str("Digite a ORIGEM da aresta: "))
                d = input(str("Digite o DESTINO da aresta: "))
                
                inserir_aresta(matriz, vertices, o, d, nao_direcionado)
                
                
            case "4":
                print("Remover vértice")
                vertice_removido = input(str("Digite o vértice que deseja remover: "))
                print(remover_vertice(matriz, vertices, vertice_removido))
            
            
            case "5":
                print("Remover aresta")
                o = input(str("Digite a ORIGEM da aresta: "))
                d = input(str("Digite o DESTINO da aresta: "))
                
                remover_aresta(matriz, vertices, o, d, nao_direcionado)
            
            
            case "6":
                print("Verificar se a aresta existe no grafo")
                o = input(str("Digite a ORIGEM da Aresta: "))
                d = input(str("Digite o DESTINO da Aresta: "))
                
                aresta = existe_aresta(matriz, vertices, o, d)
                
                if aresta:
                    print(f"A resta [{o}, {d}] está no grafo.")
                else:
                    print(f"A resta [{o}, {d}] não existe.")
                
                
            case "7":
                print("Grau de um vértice no grafo")
                g = grau_vertices(matriz, vertices)
                
                print(g)
            
            
            case "8":
                print("Verificar se o percurso válido")
                p =  input(str("Digite o percurso: "))
                
                per = p.split(", ")
                percurso = percurso_valido(matriz, vertices, per)
                
                if percurso:
                    print("É um percurso válido!")
                else:
                    print("Não é um percurso válido!")
                
                
            case "9":
                print("Listar todos os vizinhos")
                vertice = input(str("Digite o vertice: "))
                
                listar_vizinhos(matriz, vertices, vertice)

                
            case "0":
                print("Fim!")
                continuar = False   
            


if __name__ == "__main__":
    matriz, vertices = criar_grafo()
    main()
