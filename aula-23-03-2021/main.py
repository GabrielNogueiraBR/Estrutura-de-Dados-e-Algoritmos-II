# Criando uma Classe em Python
class Grafo:
    
    # Metodo construtor passando 'self' para referenciar o proprio objeto
    def __init__(self):
        self.vertices = []
        self.arestas = {}
        self.pesos = {}
        
    def adiciona_vertice(self, valor):
        self.vertices.append(valor)
        self.arestas[valor] = []
        
    def adiciona_aresta(self, origem, destino, peso):
        
        if origem not in self.vertices:
            self.adiciona_vertice(origem)
        
        if destino not in self.vertices:
            self.adiciona_vertice(destino)
        
        self.arestas[origem].append(destino)
        #self.arestas[destino].append(origem) # Caso seja um grafo sem direcao
        self.pesos[(origem,destino)] = peso



#####################        



#####################

g = Grafo()

g.adiciona_aresta("S", "A", 1)
g.adiciona_aresta("S", "B", 5)
g.adiciona_aresta("A", "B", 2)
g.adiciona_aresta("A", "C", 2)
g.adiciona_aresta("A", "D", 1)
g.adiciona_aresta("B", "D", 2)
g.adiciona_aresta("C", "D", 3)
g.adiciona_aresta("C", "E", 1)
g.adiciona_aresta("D", "E", 2)

print(g.vertices)
print(g.arestas)
print(g.pesos)
