### mapa do maroto
### estrutura de dados 2

### utilize um mapa inicialmente, depois faça o código rodar em todos eles

""" Mapa 1
>....v
"""

mapa1 = {'h': 6, 'v': 1, 'info': '>....v'}

""" Mapa 2
>.....v
.......
v.....<
...*...
>......
"""

mapa2 = {'h': 7, 'v': 5, 'info': '>.....v.......v.....<...*...>......'}



v = 0
strMapa = ""
vertices = []

while v < mapa2['v']:
    h = 0
    
    while h < mapa2['h']:
        valor = mapa2['info'][(h + (mapa2['h']*v))]
        
        if(valor != "."):
            vertice = {}
            vertice['nome'] = "V" + str(len(vertices))
            vertice['valor'] = valor
            vertice['posicao'] = h + (mapa2['h']*v)
            vertices.append(vertice)

        strMapa = strMapa + valor
        h = h + 1

    strMapa = strMapa + "\n"
    v = v + 1

print(vertices)
""" Mapa 3
>.v.
....
*.v.
....
..^.
"""

mapa3 = {'h': 4, 'v': 5, 'info': '>.v.....*.v.......^.'}

""" Mapa 4
>.....v..v
>....*....
^.....<..^
"""

mapa4 = {'h': 10, 'v': 3, 'info': '>.....v..v>....*....^.....<..^'}


# DICAS:
#
# (1) pense como ler os dados do mapa e transformar em um grafo, (os mapas são dicionários) 
#     cada direção é um vértice e aponta com qual vértice seguinte se conecta
#
# (2) as arestas não devem ser utilizadas duas vezes para eles não se perderem no castelo
#
# (3) utilize papel e caneta para verificar se as informações de vértices e arestas estão corretas
#     a medida que você implementar
#
# (4) ao final, basta imprimir qual é o mapa CORRETO, para todos os outros apenas ignore

