def comprar(indice, acao, saldo ):
    # Caso seja o primeiro dia nao iremos comprar
    if(indice == 0):
        return False, 0
    else:
        desvalorizacao = precoMedioAcao(indice,acao)/acao[indice-1]
        desvalorizavao = (1 - desvalorizacao) * 100

        if(desvalorizacao < 6):
            return True, (saldo//acao[indice])
        
        if(desvalorizacao > 6):
            return False, 0

def precoMedioAcao( indice, acao):
    cont = 0
    soma = 0
    
    while cont < indice:
        soma += acao[cont]
        cont+= 1
    
    return (soma/(cont+1))

def vender(indice, acao, qtd_acao):
    # Caso seja o primeiro dia nao iremos vender
    if(indice == 0):
        return False, 0
    else:
        valorizacao = precoMedioAcao(indice,acao)/acao[indice-1]
        valorizacao = (1 - valorizacao) * 100

        if(valorizacao > 6):
            return True, (qtd_acao)
        
        if(valorizacao < 6):
            return False, 0


# Exercicio de fixacao:

acoes = 0
carteira = 100

FACN = [8.50,8.0,9.0,8.5,8.5,9.0,8.0,7.0]

# O lucro de um investimento eh definido na hora da compra e nao da venda.

for index, valor in enumerate(FACN):
    # Chamada da funcao para verificar se ira comprar algum item
    compra, qtd_compra = comprar(index,FACN,carteira)
    
    # Codigo para fazer a compra
    if(compra):
        carteira -= valor * qtd_compra
        acoes += qtd_compra
    
    # Chamada da funcao para verificar se vai vender algum item
    venda, qtd_venda = vender(index,FACN,acoes)
    if(venda):
        carteira += valor * qtd_venda
        acoes -= qtd_venda

if(acoes > 0):
    carteira += acoes * valor
    acoes = 0

print(carteira)

