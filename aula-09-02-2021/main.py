'''
Comentarios pode ser feitos com a # (uma linha apenas) ou com três aspas simples 

'''

# Troca de valores entre variaveis de maneira simplificada
a = 5
b = 3

a,b = b,a

print(a,b)

# Utilizando True e False em Python
a = True
b = False
c = 5 < 3

print(a == c)

# Interpolacao de string em Python
nome = "Gabriel"
idade = 20

print("O nome é %s e tem %i anos." %(nome,idade)) # Primeira maneira
print(f"O nome é {nome} e tem {idade} anos.") # Segunda maneira

# Recebendo valores em um input
nome = input("Digite um nome: ")

# O input recebe ate mesmo valores que sao carregados no momento em que o python é carregado. 
# Por exemplo, na linha abaixo vemos um comando para que o arquivo main.py carregue o arquivo.txt quando se inicia o programa
# O input também pode ser utilizado após esse comando para pegar os valores dentro dele e utilizar durante o código
# python main.py < arquivo.txt
# input() - Lê as informacoes do arquivo.txt

# Toda entrada de buffer é do tipo texto, portanto, para executar qualquer operação é necessário utilizar um CAST
a = input("Digite um número: ")
b = input("Digite um número: ")

print(a+b)
print(type(a))
print(type(b))
print(int(a)+int(b))

# Operadores aritmeticos

print(3//2) # 
print(10%5) # Resto da divisao

# Estruturas condicionais em Python
a = 3
b = 2

if a > b:
    print("a é maior.")
elif a == b:
    print("a é igual a b")
else:
    print("b é maior.")

# Operador OR
if (a > b) or (b > a):
    print("Operador OR")

# Operador AND
if (a > b) and (b < a):
    print("Operador AND")

# Validando o maior/menor dentre vários valores
if (5 > 3 > 2):
    print("O valor 5 é maior de todos")

'''
OBSERVAÇÃO: CASO A IDENTAÇÃO SEJA DIFERENTE EM ALGUMA PARTE DO CODIGO, O PROGRAMA VAI APONTAR UM ERRO. 
POR EXEMPLO, CASO EU COPIE UM EXEMPLO COM IDENTAÇÃO COM TRÊS ESPAÇOS E EU ESTEJA UTILIZANDO 
UMA IDENTAÇÃO COM QUATRO ESPAÇOS NO CÓDIGO, A EXECUÇÃO VAI RETORNAR UM ERRO.
'''

# Operadores unitários de incremento e decremento não existem em python, exemplo:
# i++
# ++i
# i--
# --i
# No Python devemos fazer da seguinte maneira:

i = 4
i += 1 # resulta em 5

# Criando um dicionário em Python

a = dict() # Dicionário - Primeira forma de instanciar
a = {"nome": "Gabriel"} # Dicionário - Segunda forma de instanciar
a["idade"] = 20 # adicionando itens ao dicionario
print(a)

# Funcoes em Python

def soma(a,b):
    return a + b

print(soma(1,2)) # Chamada da funcao em Python

# Funcao em Python retornando mais de um valor
def soma(a,b):
    return a + b, a, b

resultado, valorA, valorB = soma (1,2)
print(f"O resultado de {valorA} + {valorB} é igual a {resultado}")

resultado, valorA, _ = soma (1,2) # O undrscore em Python ignora o ultimo valor retornado da funcao soma que retorna tres valores, ou seja, o valor de b

# Funcao com valores padroes
def dividir(a , b = 1):
    return a/b, a, b

resultado, valorA, valorB = dividir(5)

print(f"O resultado de {valorA} / {valorB} é igual a {resultado}")

'''
Exercícios:

1) O maior entre três números.
2) Read two nteger values (A and B). After, the program should print the message "Sao Multiplos" (are multiples) or "Nao sao Multiplos" (aren’t multiples), corresponding to the read values.
3) Elabore um código que traduza as funcionalidades dos exercícios 1 e 2 em duas funções, uma para encontrar o maior entre 2 números; e outra para verificar se dois números são múltiplos.
'''
valorA = input()
valorB = input()
valorC = input()

def maior(a,b,c):
    if(a>b>c):
        print(f"O valor {a} eh o maior.")
    elif(b>a>c):
        print(f"O valor {b} eh o maior.")
    else:
        print(f"O valor {c} eh o maior.")

print(maior(int(valorA),int(valorB),int(valorC)))

def multiplos(a,b):
    if((a%b) == 0):
        print(f"Os valores {a} e {b} sao multiplos.")
    else:
        print(f"Os valores {a} e {b} nao sao multiplos.")

valorA = input()
valorB = input()

print(multiplos(int(valorA),int(valorB)))
