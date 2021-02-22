# Criação de uma lista em Python
alunos = ['Guilherme','Rafael','Gabriel']

print('\nExibindo a frequencia de um elemento na lista')
print(alunos.count('Guilherme')) # retorna 1

# Acessando um elemento de uma lista atraves do indice
print(alunos[0])

# Criando uma lista dentro de outra lista (matriz)
matriz = [[1,2],[3,4]]

# Acessando o primeiro elemento de uma lista
print(matriz[0])

# Acessando o primeiro valor do primeiro elemento da lista
print(matriz[0][0])

matriz = []

# O append faz a insercao dos itens na ordem em que eles foram inseridos, de forma que a matriz fique 1, 2, 3 e 4
matriz.append(1)
matriz.append(2)
matriz.append(3)
matriz.append(4)

print(matriz)

matriz = []

# O insert posiciona o elemento na lista na posicao que informarmos, de modo que a sequencia abaixo fique 4,3,2 e 1.
matriz.insert(0,1)
matriz.insert(0,2)
matriz.insert(0,3)
matriz.insert(0,4)

# Retira o ultimo elemento da lista
matriz.pop()

# Retira o elemento de indice um para ser retirado da lista
matriz.pop(1)

# Retira o elemento com base no valor do elemento, ou seja, o comando a seguir vai retirar o elemento com valor "2" da lista, esteja ele em qualquer posicao
matriz.remove(2)

# Retorna para o indice do elemento passado via parametro da funcao infex()
matriz.index(1)

# Tamanho da matriz
print(len(matriz))