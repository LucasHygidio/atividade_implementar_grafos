from collections import deque

from busca_largura_padrao_lista_aresta import (
    criar_grafo,
    inserir_aresta,
    remover_aresta,
    exibir_grafo,
    bfs_lista_aresta,
    grau_vertices,
    vizinhos
)

def bfs_para_caminho_curto(vertices, arestas, inicio):
    if inicio not in vertices:
        return {} 

    fila = deque([inicio])
    predecessores = {inicio: None}

    while fila:
        vertice_atual = fila.popleft()
        lista_vizinhos = vizinhos(vertices, arestas, vertice_atual)
        
        for vizinho in lista_vizinhos:
            if vizinho not in predecessores:
                predecessores[vizinho] = vertice_atual
                fila.append(vizinho)
                
    return predecessores


def encontrar_menor_caminho(vertices, arestas, inicio, fim):
    predecessores = bfs_para_caminho_curto(vertices, arestas, inicio)
    
    if fim not in predecessores:
        return None 

    caminho = []
    no_atual = fim
    
    while no_atual is not None:
        caminho.append(no_atual)
        no_atual = predecessores[no_atual] 
        
    caminho.reverse()
    
    if caminho[0] == inicio:
        return caminho
    else:
        return None 

def menu_interativo(vertices, arestas, nao_direcionado):
    continuar = True
    
    while continuar:
        print("""
              1 - Exibir o Grafo
              2 - Inserir Aresta
              3 - Remover Aresta
              4 - Executar Busca em Largura (Ordem de Visita)
              5 - Encontrar Menor Caminho
              6 - Verificar Grau dos Vértices
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
                remover_aresta(arestas, arestas, o, d, nao_direcionado)
                print(f"Aresta {o} -> {d} removida (se existia).")
            
            case "4":
                if not vertices:
                    print("O grafo está vazio.")
                    break
                inicio = input(str("Digite o VÉRTICE INICIAL para o BFS: "))
                if inicio not in vertices:
                    print(f"Erro: O vértice '{inicio}' não existe.")
                    break
                
                resultado = bfs_lista_aresta(vertices, arestas, inicio)
                if resultado:
                    print(f"\nPercurso BFS (Ordem de visita): {resultado}\n")
            
            case "5":
                if not vertices:
                    print("O grafo está vazio.")
                    break
                
                inicio = input(str("Digite o VÉRTICE INICIAL do caminho: "))
                fim = input(str("Digite o VÉRTICE FINAL do caminho: "))
                
                if inicio not in vertices or fim not in vertices:
                    print(f"Erro: Vértice de início ou fim não existe no grafo.")
                    break
                    
                caminho_resultante = encontrar_menor_caminho(vertices, arestas, inicio, fim)
                
                if caminho_resultante:
                    print(f"\nMenor Caminho: {' -> '.join(caminho_resultante)}")
                    print(f"(Total de arestas: {len(caminho_resultante) - 1})")
                else:
                    print(f"\nNão foi encontrado caminho de {inicio} para {fim}.")
            
            case "6":
                grau = grau_vertices(vertices, arestas, nao_direcionado)
                print("\nGrau dos Vértices:")
                for v, g in grau.items():
                    print(f"   Vértice {v}: Entrada={g['entrada']}, Saída={g['saida']}, Total={g['total']}")
                print("")
            
            case "0":
                print("Fim!")
                continuar = False 
            
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    print("Configurando grafo de teste não direcionado...")
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