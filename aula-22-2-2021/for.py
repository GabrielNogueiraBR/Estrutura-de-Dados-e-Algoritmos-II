lista = [1,2,3,4,5]

# Percorrendo uma lista atraves de um for e printando na tela todos os seus elementos.
for elemento in lista:
    print(elemento)

alunos = ['Gabriel','Rafael','Miguel']

for aluno in alunos:
    variavel = 'Continuo existindo fora do for'
    print(aluno)

# Um detalhe importante de se atentar ao Python, eh em relacao ao escopo do projeto. Por exemplo, aluno continua existindo mesmo apos a saida do loop do for
print(aluno)

# Outro ponto eh que se uma variavel for definida dentro do laco do for, ela continua existindo depois
print(variavel)

# Como deletar uma variavel
del variavel

alunos = ['Gabriel','Rafael','Miguel','Rodrigo','Leandro']

print('\nParando o laco de repeticao for em determinado momento')
# Como obter o indice e o valor de um elemento em uma lista com o laco do for
# 0 Gabriel
# 1 Rafael
# 2 Miguel
for indice, nomeAluno in enumerate(alunos):
    if nomeAluno == 'Rodrigo':
        break
    print(indice, nomeAluno)

print('\nPulando uma execucao de codigo no for')
# 0 Gabriel
# 1 Rafael
# 2 Miguel
# 4 Leandro
for indice, nomeAluno in enumerate(alunos):
    if nomeAluno == 'Rodrigo':
        continue
    print(indice, nomeAluno)

print('\nAlterando os valores dentro da lista alunos')
# 0 Gabriel
# 1 Rafael
# 2 Miguel
# 3 Ronaldo
# 4 Leandro
for indice, nomeAluno in enumerate(alunos):
    if nomeAluno == 'Rodrigo':
        alunos[indice] = 'Ronaldo'
    print(indice, nomeAluno)

print('\nUtilizando o in range()')
for x in range(10):
    print(x)