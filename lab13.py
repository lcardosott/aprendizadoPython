def adiciona(relacao_diretorios, local, diretorio, aux, nome):
    ''' Funcao responsavel por criar um diretorio 
    '''
    if local[aux] in relacao_diretorios or aux == len(local): #Caso o diretorio até determinada pasta já exista, ou o programa ja tenha percorrido toda a lista local
        diretorio = relacao_diretorios[local[aux]] + '_' + diretorio 
        relacao_diretorios[nome] = diretorio #Armazena o diretorio criado para ser utilizado futuramente
        return diretorio

    else:
        diretorio = local[aux] + '_' + diretorio    
        aux +=1
        return adiciona(relacao_diretorios, local, diretorio, aux)

def main():
    pasta, quantidade_arquivos = input().split()
    relacao_diretorios = {}
    relacao_diretorios [pasta] = pasta
    
    for i in range(int(quantidade_arquivos)):
        nome, local = input().split(' ', 1)
        local, diretorio, aux = local.split(), nome, 0
        print (adiciona(relacao_diretorios, local, diretorio, aux, nome))

if __name__ == '__main__':
    main()
