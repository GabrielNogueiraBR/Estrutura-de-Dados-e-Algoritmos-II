def BFS(G, s):

    distancias = {}
    visitados = []
    caminhos = {}

    distancias[s] = 0
    visitados = [s]
    caminhos[s] = [s]
    fila = [s]

    while len(fila) > 0:
        u = fila.pop(0) 

        for v in G[u]: # pra cada adjacencia u---v
            if v not in visitados:
                visitados.append(v)
                distancias[v] = distancias[u] + 1
                caminhos[v] = []
                for c in caminhos[u]:
                    caminhos[v].append(c)
                caminhos[v].append(v)
                fila.append(v)

    return visitados, distancias, caminhos

#############################################

G = {
  'A' : ['B','C','D'],
  'B' : ['A', 'E'],
  'C' : ['A','G'],
  'D' : ['A','H'],
  'E' : ['B'],
  'F' : [],
  'G' : ['C','H'],
  'H' : ['D','G','I'],
  'I' : ['H']
}

visitados, distancias, caminhos = BFS(G, 'A')
print(visitados)
print(distancias)
print(caminhos)