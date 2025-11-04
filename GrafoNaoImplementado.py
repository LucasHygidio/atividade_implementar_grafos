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
        
def exibir_grafo(grafo):
    for chave in grafo:
        print(f"{chave} -> {vizinhos(grafo, chave)}")


def remover_aresta(grafo, origem, destino, nao_direcionado=False):
    """
    Remove a aresta entre origem e destino.
    Passos:
    1. Verificar se 'origem' existe; se não, terminar.
    2. Se destino estiver em grafo[origem], remover essa ocorrência.
    3. Se for não direcionado, também:
         - verificar se 'destino' existe e remover 'origem' de grafo[destino] se presente.
    """
    
    if (origem not in grafo.keys()):
        return "Origem não existente no grafo"
    
    if destino in grafo[origem]:
        if nao_direcionado:
            grafo[destino].remove(origem)
        grafo[origem].remove(destino)


def remover_vertice(grafo, vertice, nao_direcionado=True):
    """
    Remove um vértice e todas as arestas que o tocam.
    Passos:
    1. Verificar se 'vertice' existe em grafo; se não, terminar.
    2. Para cada outro vertice no grafo:
         - se 'vertice' estiver na lista de vizinhos, remover essa aresta.
    3. Remover o vertice do grafo
    4. Opcional: retornar confirmação/erro.
    """
    pass


def existe_aresta(grafo, origem, destino):
    """
    Verifica se existe aresta direta origem -> destino.
    Passos:
    1. Verificar se 'origem' é chave no grafo.
    2. Retornar True se 'destino' estiver em grafo[origem], caso contrário False.
    """
    pass

def grau_vertices(grafo):
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
    continuar = True
    
    while continuar:
        print("""
                1 - Mostrar o Grafo
                2 - inserir vertice
                3 - inserir aresta
                4 - remover vértice.
                0 - Sair
              """)
        opcao = input(str("\nEscolha uma opção: "))
        
        match opcao:
            case "1":
                print("Mostrar o Grafo\n")
                
                exibir_grafo(grafo1)
                
            case "2":
                print("Inserir vertice\n")
                vertice = input(str("Digite o valor do Vertice: "))
                
                inserir_vertice(grafo1, vertice)
                
            case "3":
                print("Inserir aresta\n")
                aresta_origem = input(str("Digite a ORIGEM da aresta: "))
                aresta_destino = input(str("Digite o DESTINO da aresta: "))
                tipo_grafo = input(bool("*Opcional: \nDigite o tipo do grafo (Direcionado - True | Não Direcionado - False)"))
                
                inserir_aresta(grafo1, aresta_origem, aresta_destino)
                
            case "4":
                print("Remover vertice")
                vertice_removido = input(str("Digite o vertice que deseja remover: "))
                
                remover_vertice(grafo1, vertice_removido)
            
            case "0":
                print("Fim!")
                continuar = False    
                
 
if __name__ == "__main__":
    grafo1 = criar_grafo()
    main()


# grafo1 = criar_grafo()
# inserir_aresta(grafo1, "A","B", True)
# inserir_aresta(grafo1, "A","C", True)
# inserir_aresta(grafo1, "A","D")
# inserir_aresta(grafo1, "D","B")
# inserir_aresta(grafo1, "C","B")
# inserir_aresta(grafo1, "D","C")

# exibir_grafo(grafo1)

# remover_aresta(grafo1, "A", "B", True)
# print("\n----------------------\n")
# exibir_grafo(grafo1)

# print("\n----------------------\n")
# remover_vertice(grafo1, "A", False)
# exibir_grafo(grafo1)


# print("\n----------------------\n")
# print(existe_aresta(grafo1, "B", "E"))
# print(existe_aresta(grafo1, "C", "B" ))

# print("\n----------------------\n")
# print(grau_vertices(grafo1))

# print("\n----------------------\n")
# print(percurso_valido(grafo1, ["D", "C", "B"]))
# print(percurso_valido(grafo1, ["D", "C", "C"]))

