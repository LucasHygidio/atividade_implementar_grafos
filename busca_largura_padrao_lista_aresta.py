# Busca em Largura (vBreadth-First Search – BFS)
#visitar todos os vértices a partir de um vértice inicial em camadas

# Usando o deque pela fila otimizada (Reduz complexidade de tempo) -> implementado internamente como uma lista duplamente ligada
from collections import deque

# Para usar de teste para o BFS
def criar_grafo():
    """
    Inicializa o grafo retornando listas vazias para vértices e arestas.
    """
    vertices = []
    arestas = []
    return vertices, arestas

def inserir_vertice(vertices, vertice):
    """
    Adiciona um vértice ao grafo se ele ainda não existir.
    """
    if vertice not in vertices:
        vertices.append(vertice)


def inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=False):
    """
    Adiciona uma aresta (origem -> destino) ao grafo
    Caso 'nao_direcionado' for True insere a aresta de volta (destino -> origem).
    Se os vértices não existirem, eles são criados
    """
    if origem not in vertices:
        inserir_vertice(vertices, origem)
    if destino not in vertices:
        inserir_vertice(vertices, destino)
    if [origem, destino] not in arestas:
        arestas.append([origem, destino])
    if nao_direcionado and [destino, origem] not in arestas:
        arestas.append([destino, origem])


def remover_aresta(arestas, origem, destino, nao_direcionado=False):
    """
    Remove uma aresta do grafo
    Caso 'nao_direcionado' for True remove a aresta (destino -> origem) 
    """
    if [origem, destino] in arestas:
        arestas.remove([origem, destino])

    if nao_direcionado and [destino, origem] in arestas:
        arestas.remove([destino, origem])
            
            
def remover_vertice(vertices, arestas, vertice):
    """
    Remove um vértice e todas as arestas relacionadas
    """
    if vertice in vertices:
        novas_arestas = []
        for a in arestas:
            if vertice not in a:
                novas_arestas.append(a)
        arestas[:] = novas_arestas
        vertices.remove(vertice)


def existe_aresta(arestas, origem, destino):
    """
    Verifica se uma aresta específica existe no grafo e retorna True ou False.
    """
    if [origem, destino] in arestas:
        return True
    return False


def vizinhos(vertices, arestas, vertice):
    """
    Pega todos os vizinhos (vértices de destino) do vértice de origem
    """
    lista_vizinhos = []
    if vertice in vertices:
        for aresta in arestas:
            if aresta[0] == vertice:
                lista_vizinhos.append(aresta[1])
    return lista_vizinhos


def grau_vertices(vertices, arestas, nao_direcionado = False):
    """
    Calcula o grau de entrada, saída e total de cada vértice
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
    

def percurso_valido(arestas, caminho):
    """
    Verifica se um percurso é possível (seguindo as arestas na ordem dada)
    """
    for i in range(len(caminho) - 2):
        u = caminho[i]
        v = caminho[i + 1]
        
        if not existe_aresta(arestas, u, v):
            return False 

    return True  


def listar_vizinhos(vertices, arestas, vertice):
    """
    Exibe os vizinhos de um vértice, chamando a função vizinhos()
    """
    lista = vizinhos(vertices, arestas, vertice)
    
    if lista:
        print(f"Vizinhos de {vertice}: {lista}")
    else:
        print(f"O vértice '{vertice}' não possui vizinhos ou não existe.")


def exibir_grafo(vertices, arestas):
    """
    Exibe todas as arestas e vértices do grafo
    """
    print(f"Vértices: {vertices}")
    
    print("Arestas:")
    
    if not arestas:
        print("  (Grafo vazio, sem arestas)")
    else:
        for aresta in arestas:
            print(f"  {aresta[0]} -> {aresta[1]}")

def bfs_lista_aresta(vertices, arestas, inicio):
    """Faz a busca em largura em um grafo por lista de arestas

    Args:
        vertices (lista): A lista de vértices do grafo
        arestas (lista): A lista de arestas do grafo
        inicio (string): O vértice de partida para a busca
    """
    
    if inicio not in vertices:
        print(f"Erro: O vertice inicial '{inicio} não existe")
        return []
    
    fila = deque([inicio])
    visitados = {inicio}
    caminho = []
    
    while fila:
        vertice_atual = fila.popleft()
        caminho.append(vertice_atual)
        lista_vizinhos = vizinhos(vertices, arestas, vertice_atual)
        
        for i in lista_vizinhos:
            if i not in visitados:
                visitados.add(i)
                fila.append(i)
    return caminho

def menu_interativo(vertices, arestas, nao_direcionado):
    """
    Seleção manual dos vertices, areastas, etc.
    Opções:
                1 - Exibir o Grafo
                2 - Inserir Aresta
                3 - Remover Aresta
                4 - Executar Busca em Largura (BFS)
                5 - Verificar Grau dos Vértices
                0 - Sair
    """
    continuar = True
    
    while continuar:
        print("\n" + "="*40)
        print("  MENU PRINCIPAL DO GRAFO DE TESTE")
        print("="*40)
        print("""
                1 - Exibir o Grafo
                2 - Inserir Aresta
                3 - Remover Aresta
                4 - Executar Busca em Largura (BFS)
                5 - Verificar Grau dos Vértices
                0 - Sair
            """)
        
        opcao = input(str("\nEscolha uma opção: "))
        
        match opcao:
            case "1":
                exibir_grafo(vertices, arestas)
            
            case "2":
                o = input(str("Digite a ORIGEM da aresta: "))
                d = input(str("Digite o DESTINO da aresta: "))
                inserir_aresta(vertices, arestas, o, d, nao_direcionado)
                print(f"Aresta {o} -> {d} inserida.")
            
            case "3":
                o = input(str("Digite a ORIGEM da aresta a ser removida: "))
                d = input(str("Digite o DESTINO da aresta a ser removida: "))
                remover_aresta(arestas, o, d, nao_direcionado)
                print(f"Aresta {o} -> {d} removida (se existia).")
            
            case "4":
                if not vertices:
                    print("O grafo está vazio. Insira vértices primeiro.")
                    break

                inicio = input(str("Digite o VÉRTICE INICIAL para o BFS: "))
                
                if inicio not in vertices:
                    print(f"Erro: O vértice '{inicio}' não existe.")
                    break
                    
                resultado = bfs_lista_aresta(vertices, arestas, inicio)
                if resultado:
                    print(f"\n✨ Percurso BFS a partir de '{inicio}': {resultado}\n")
            
            case "5":
                grau = grau_vertices(vertices, arestas, nao_direcionado)
                print("\nGrau dos Vértices:")
                for v, g in grau.items():
                    print(f"  Vértice {v}: Entrada={g['entrada']}, Saída={g['saida']}, Total={g['total']}")
                print("")
            
            case "0":
                print("Fim!")
                continuar = False 
            
            case _:
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    print("Configurando grafo de teste não direcionado (S/N): N")
    nao_direcionado = True
    vertices, arestas = criar_grafo()
    
    inserir_aresta(vertices, arestas, 'A', 'B', nao_direcionado)
    inserir_aresta(vertices, arestas, 'B', 'C', nao_direcionado)
    inserir_aresta(vertices, arestas, 'C', 'A', nao_direcionado)
    inserir_aresta(vertices, arestas, 'B', 'D', nao_direcionado)
    inserir_aresta(vertices, arestas, 'D', 'E', nao_direcionado)

    print("Grafo de teste carregado automaticamente com os vértices: A, B, C, D, E.")
    exibir_grafo(vertices, arestas)
    
    menu_interativo(vertices, arestas, nao_direcionado)