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
        return lista_vizinhos
    else:
        print(f"Vértice '{vertice}' não encontrado")
  
        
def exibir_grafo(grafo):
    for chave in grafo:
        print(f"{chave} -> {vizinhos(grafo, chave)}")


def remover_aresta(grafo, origem, destino, nao_direcionado=False):

    if (origem not in grafo.keys()):
        return "Origem não existente no grafo"
    
    if destino in grafo[origem]:
        if nao_direcionado:
            grafo[destino].remove(origem)
        grafo[origem].remove(destino)


def remover_vertice(grafo, vertice, nao_direcionado=True): #Revisar
    
    if (vertice not in grafo.keys()):
        return "Vertice não existente no grafo"
    
    if(vertice in grafo.keys()):       
        for no in grafo.keys():   
            remover_aresta(grafo, no, vertice)
    grafo.pop(vertice)
        

def existe_aresta(grafo, origem, destino):

    if (origem in grafo.keys() and destino in grafo.keys()):
        if destino in grafo[origem]:
            return True
        else:
            return False
    else:
        return f"Não existe o vertice '{origem}' no grafo!"
        
        

def grau_vertices(grafo):
    #OUT, IN, TOTAL
    
    graus = {}
    
    for no in grafo:
        in_degree = 0
        out_degree = 0
        total = 0
        
        out_degree = len(grafo[no])
        
        for aresta in grafo.values():
            if no in aresta:
                in_degree += 1
        
        total = out_degree + in_degree
        graus[no] = (out_degree, in_degree, total)

    return graus
    

def percurso_valido(grafo, caminho):
    if len(caminho) < 2:
        return True
    
    for i in range (len(caminho) -1):
        origem = caminho[i]
        destino = caminho[i+1]
            
        if existe_aresta(grafo, origem, destino) == False:
            return False
            
    return True


def main():
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
                
                inserir_aresta(grafo1, aresta_origem, aresta_destino, nao_direcionado)
                
            case "4":
                print("Remover vertice")
                vertice_removido = input(str("Digite o vertice que deseja remover: "))
                
                remover_vertice(grafo1, vertice_removido, nao_direcionado)
            
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

