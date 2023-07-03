def selecao(largura, altura, matriz, selecionado, cordenadacoluna, cordenadalinha):
    ''' A função tem o objetivo de selecionar uma determinada área de uma matriz'''
    for j in range(altura):
        aux = []
        for i in range(largura):
            aux.append(matriz[cordenadalinha+j][cordenadacoluna+i])
        selecionado.append(aux)

def espelhamento(comando, matriz):
    ''' A função tem o objetivo de espelhar uma determinada matriz tanto na horizontal quanto na vertical '''
    nova = []
    if comando[1] == 'h':
        for i in range(len(matriz)):
            aux = []
            for j in range(len(matriz[0])):
                aux.append(matriz[i][-1-j])
            nova.append(aux)
    else:
        for i in range(len(matriz)):
            nova.append(matriz[-1-i])
    return nova

def rotacao(matriz):
    ''' A função tem o objetivo de rotacionar uma determinada matriz
    '''
    nova = []
    for j in range(len(matriz[0])):
        aux= []
        for k in range(len(matriz)):
            aux.append(matriz[-1-k][j])
        nova.append(aux)
    return nova

def copia(selecionado, matriz, comando):
    ''' A função tem objetivo de copiar um 'fragmento' de matriz, e cola-la em um ponto de outra
    '''
    iniciocoluna, iniciolinha = int(comando[1]), int(comando[2])
    for i in range(len(selecionado)):
        for j in range(len(selecionado[0])):        
            matriz[iniciolinha+i][iniciocoluna+j] = selecionado[i][j]

def recorte(selecionado, matriz, comando, cordenadacoluna, cordenadalinha):
    ''' A função tem o objetivo de substituir uma determinada área pelo valor '000' e colar esse trecho em outro ponto 
    '''
    for i in range(len(selecionado)):
        for j in range(len(selecionado[0])):
            matriz[cordenadalinha+i][cordenadacoluna+j] = '000'
    iniciocoluna, iniciolinha = int(comando[1]), int(comando[2])
    for i in range(len(selecionado)):
        for j in range(len(selecionado[0])):
            matriz[iniciolinha+i][iniciocoluna+j] = selecionado[i][j]

def insere(matriz, cordenadacoluna, cordenadalinha, objeto):
    ''' A função tem o objetivo de interir um 'fragmento' de matriz em outra
    '''
    for i in range(len(objeto)):
        for j in range(len(objeto[0])):
            matriz[cordenadalinha+i][cordenadacoluna+j] = objeto[i][j]

def zera(matriz, cordenadacoluna, cordenadalinha, largura, altura):
    ''' A função tem o objetivo de substituir uma determinada área pelo valor '000' (utilizada em conjunto com a função 'rotaciona')
    '''
    for i in range(altura):
        for j in range(largura):
            matriz[cordenadalinha+i][cordenadacoluna+j] = '000'    

largura, altura = map(int, input().split())
n = int(input())
oficial = []
selecionado = []
for i in range(altura):
    auxiliar = input().split()
    oficial.append(auxiliar)

for i in range(n):
    funcao = input().split()
    if funcao[0] == 'selecao':
        selecionado = []
        cordenadacoluna, cordenadalinha, largura, altura = int(funcao[1]), int(funcao[2]), int(funcao[3]), int(funcao[4])    
        selecao(largura, altura, oficial, selecionado, cordenadacoluna, cordenadalinha)

    elif funcao[0] == 'rotacao':
        if selecionado == []:
            oficial = rotacao(oficial)
        else:
            zera(oficial, cordenadacoluna, cordenadalinha, largura, altura)
            rotacionado = rotacao(selecionado)
            insere(oficial, cordenadacoluna, cordenadalinha, rotacionado)

    elif funcao[0] == 'copia':
            copia(selecionado, oficial, funcao)

    elif funcao[0] == 'recorte':
            recorte(selecionado, oficial, funcao, cordenadacoluna, cordenadalinha)

    elif funcao[0] == 'espelhamento':
        if selecionado == []:
            oficial = espelhamento(funcao, oficial)
        else:
            espelhado = espelhamento(funcao, selecionado)
            insere(oficial, cordenadacoluna, cordenadalinha, espelhado)

    if selecionado != []:
        selecionado = []
        selecao(largura, altura, oficial, selecionado, cordenadacoluna, cordenadalinha)

for i in range(len(oficial)):
    print (*oficial[i])