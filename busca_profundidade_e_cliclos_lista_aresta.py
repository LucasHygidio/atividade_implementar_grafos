#Busca em profundidade
from collections import deque

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

def dfs(vertices, arestas, inicio):
    """
    Implementação da DFS
    """
    
    if inicio not in vertices:
        print(f"Erro: O vértice '{inicio}' não existe.")
        return []

    pilha = [inicio]
    visitados = []
    while pilha:
        
        vertice_atual = pilha.pop()
        if vertice_atual not in visitados:
            visitados.append(vertice_atual)
            lista_vizinhos = vizinhos(vertices, arestas, vertice_atual)

            for vizinho in reversed(lista_vizinhos):
                if vizinho not in visitados:
                    if vizinho not in pilha:
                        pilha.append(vizinho)

    return visitados

def detectar_ciclo_dfs(vertices, arestas, inicio):
    """
    Detecta os ciclos com dfs
    """
    if inicio not in vertices:
        print(f"Erro: Vértice {inicio} inválido.")
        return False

    pilha = [(inicio, None)]
    visitados = []
    
    mapa_pais = {inicio: None}

    while pilha:
        vertice_atual, pai = pilha.pop()

        if vertice_atual not in visitados:
            visitados.append(vertice_atual)

            lista_vizinhos = vizinhos(vertices, arestas, vertice_atual)

            for vizinho in reversed(lista_vizinhos):
                
                esta_na_pilha = any(vizinho == item[0] for item in pilha)
                ja_visitado = vizinho in visitados

                if not esta_na_pilha and not ja_visitado:
                    pilha.append((vizinho, vertice_atual))
                    mapa_pais[vizinho] = vertice_atual
                
                else:
                    if vizinho != pai:
                        print(f"\n>>> CICLO DETECTADO! Aresta que fechou: {vertice_atual} -> {vizinho}")
                        
                        
                        caminho_ciclo = [vertice_atual]
                        temp = vertice_atual
                        
                        while temp != vizinho and temp is not None:
                            temp = mapa_pais[temp]
                            if temp is not None:
                                caminho_ciclo.append(temp)
                        
                        caminho_ciclo.reverse()
                        
                        caminho_ciclo.append(vizinho) 

                        print(f"Caminho do Ciclo: {caminho_ciclo}")
                        return True

    return False

def menu_interativo(vertices, arestas, nao_direcionado):
    continuar = True
    while continuar:
        print("\n" + "="*40)
        print("  MENU PRINCIPAL")
        print("="*40)
        print("1 - Exibir Grafo\n2 - Inserir Aresta\n3 - Remover Aresta")
        print("4 - DFS (Profundidade)")
        print("5 - Graus dos Vértices")
        print("6 - Detectar Ciclo (DFS)") # NOVA OPÇÃO
        print("0 - Sair")
        
        
        opcao = input("\nOpção: ")
        
        match opcao:
            case "1": exibir_grafo(vertices, arestas)
            case "2": 
                inserir_aresta(vertices, arestas, input("Origem: "), input("Destino: "), nao_direcionado)
            case "3": 
                remover_aresta(arestas, input("Origem: "), input("Destino: "), nao_direcionado)
            case "4": 
                print(dfs(vertices, arestas, input("Início DFS: ")))
            case "5":
                print(grau_vertices(vertices, arestas, nao_direcionado))
            case "6":
                v_inicial = input("Vértice Inicial para verificação: ")
                if detectar_ciclo_dfs(vertices, arestas, v_inicial):
                    print(">>> O Grafo POSSUI Ciclo! <<<")
                else:
                    print(">>> O Grafo NÃO possui Ciclo. <<<")
            
            case "0": continuar = False
            case _: print("Inválido.")


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