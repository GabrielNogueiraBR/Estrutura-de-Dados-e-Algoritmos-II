class Grafo:
    
    def __init__(self):
        self.vertices = []
        self.arestas = {}
        self.pesos = {}

    def adiciona_vertice(self,valor):
        self.vertices.append(valor)
        self.arestas[valor] = []
    
    def adiciona_aresta(self,origem,destino,peso):
        
        if origem not in self.vertices:
            self.adiciona_vertice(origem)
        
        if destino not in self.vertices:
            self.adiciona_vertice(destino)
        
        # Adicionando as arestas do grafo nao direcionado
        self.arestas[origem].append(destino)
        self.arestas[destino].append(origem)

        # Adicionando o peso da aresta
        self.pesos[(origem,destino)] = peso
        self.pesos[(destino,origem)] = peso

def menor_distancia (T,distancias):
    vertice_menor_distancia = None
    menor_distancia = None

    for vertice in T:
        if menor_distancia is None or distancias[vertice] < menor_distancia:
            vertice_menor_distancia = vertice
            menor_distancia = distancias[vertice]

    return vertice_menor_distancia

def dijkstra (grafo, origem):
    
    dist = {}
    dist[origem] = 0
    T = []
    T.append(origem)
    P = []

    while len(T) > 0:
        
        v = menor_distancia(T,dist)
        
        T.pop(T.index(v))
        P.append(v)

        for u in grafo.arestas[v]:

            if u in T:
                dist[u] = min(dist[u], dist[v] + grafo.pesos[(u,v)])
            
            elif u not in P:
                dist[u] = dist[v] + grafo.pesos[(v,u)]
                T.append(u)
    return dist

def adiciona_rotas_aereas(grafo):
    grafo.adiciona_aresta('Petalburg','Verdanturf',7)
    grafo.adiciona_aresta('Dewford','Littleroot',5)
    grafo.adiciona_aresta('Dewford','Pacifidlog',16)
    grafo.adiciona_aresta('Pacifidlog','Mauville',12)
    grafo.adiciona_aresta('Pacifidlog','Fortree',14)
    grafo.adiciona_aresta('Pacifidlog','Mossdeep',14)
    grafo.adiciona_aresta('Mauville','Lavaridge',6)
    grafo.adiciona_aresta('Mauville','Lilycove',6)

    return grafo

def adiciona_rotas_aquaticas(grafo):
    grafo.adiciona_aresta('Petalburg','Dewford',9)
    grafo.adiciona_aresta('Dewford','Slateport',20)
    grafo.adiciona_aresta('Slateport','Pacifidlog',11)
    grafo.adiciona_aresta('Pacifidlog','Ever Grand',15)
    grafo.adiciona_aresta('Pacifidlog','Sootopolis',17)
    grafo.adiciona_aresta('Ever Grand','Lilycove',13)
    grafo.adiciona_aresta('Sootopolis','Mossdeep',8)
    grafo.adiciona_aresta('Sootopolis','Lilycove',6)
    grafo.adiciona_aresta('Lilycove','Mossdeep',6)

    return grafo

def menor_rota_recursiva(grafo, dist, vertice):
    
    if dist[vertice] == 0:
        list = []
        list.append(vertice)
        return list
    else:
        for u in grafo.arestas[vertice]:
            if dist[vertice] == (dist[u] + grafo.pesos[(u,vertice)]):
                list = menor_rota_recursiva(grafo,dist,u)
                list.append(u)
                return list
        

def menor_rota (grafo, origem, destino, usar_aereo, usar_aquatico):
    
    if usar_aereo is True:
        # Adiciona rotas aereas no grafo
        grafo = adiciona_rotas_aereas(grafo)

    if usar_aquatico is True:
        # Adiciona rotas aquaticas no grafo
        grafo = adiciona_rotas_aquaticas(grafo)

    dist = dijkstra(grafo, origem)
    menor_rota = menor_rota_recursiva(grafo,dist,destino)
    menor_rota.append(destino)

    return menor_rota
    # Aplicar o conceito reverso visto nas aulas de eletiva I

#########################################################################

g = Grafo()

# Adicionando os vertices e arestas no grafo (apenas rotas terrestres)
g.adiciona_aresta('Petalburg','Oldale',2)
g.adiciona_aresta('Petalburg','Rustboro',6)
g.adiciona_aresta('Oldale','Littleroot',5)
g.adiciona_aresta('Rustboro','Verdanturf',4)
g.adiciona_aresta('Rustboro','Fallarbor',9)
g.adiciona_aresta('Verdanturf','Mauville',2)
g.adiciona_aresta('Fallarbor','Mauville',19)
g.adiciona_aresta('Mauville','Slateport',8)
g.adiciona_aresta('Mauville','Fortree',9)
g.adiciona_aresta('Fortree','Lilycove',7)

menor_rota_grafo = menor_rota(g,'Dewford','Mossdeep',False,True)
print(menor_rota_grafo)
