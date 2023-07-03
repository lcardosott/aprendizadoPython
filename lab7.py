if __name__ == '__main__':

    def contagem(lista_base, relacao):                      #insere na lista "relacao" a quantidade de vezes que um item da "lista_base" se repete consecutivamente
        contador = 1
        for i in range((len(lista_base)) - 1):                     
            if lista_base[i] == lista_base[i+1]:
                contador +=1
            else:
                relacao[i] = contador
                contador = 1
        relacao[-1] = contador

    def compara(lista_base, relacao):                       #compara qual dos itens se repete mais vezes, e entrão, retorna quantas vezes ele se repete
        maior = 1
        for k in range(len(lista_base)):
            if relacao[k] > maior:
                maior = relacao[k] 
        return maior
  
    def unicos(lista_base,aparicao,unico):                  #com base nas aparições conta quantos itens na lista inicial são únicos
        for i in range(len(lista_base)):
            if aparicao[i]==1:
                unico += 1
        return unico

    def remover(lista_base,aparicao,remover):               #remove da lista inicial, o item separado por '/' e itens repetidos
        aux = 0
        for i in range(len(lista_base)):
            if aparicao[i] != 1:
                del lista_base[i-aux]
                aux += 1
        while True:
            try:
                lista_base.remove(remover)
                break
            except ValueError:
                break

    def trata_string(lista_base):                           #deixa todas as letras de todos os itens da lista em minúsculo, e troca ' ' por '-'
        for i in range(len(lista_base)):
            lista_base[i] = lista_base[i].lower()
            lista_base[i] = lista_base[i].replace(' ', '-')

    relação = []
    unico = 0
    l_aparicao =  []
    l_cc = []
    l_cr = []      
    l_ha = []

    inicial = input().split(', ')                           #transforma os dados inseridos numa lista
    inicial[-1], a_remover = inicial[-1].split ('/ ')         #retira do ultimo item da lista, qual foto devera ser removida
    
    for j in range(len(inicial)):                           #cria uma lista com 0's, do tamanho de inicial
        relação.append(0)
        l_aparicao.append(0)

    for i in range(len(inicial)):                           #mostra quais itens foram os primeiros a aprecer 
        if i == inicial.index(inicial[i]):
            l_aparicao[i] = 1

    contagem (inicial, relação)
    maior = compara(inicial, relação)
    print (inicial[(relação.index(maior))], maior)
    print (unicos(inicial,l_aparicao,unico))
    remover(inicial,l_aparicao,a_remover)
    trata_string (inicial)

    for i in range(len(inicial)):
        if 'cr_' in inicial[i]:
            inicial[i] = inicial[i].replace('cr_', 'CR_')
            l_cr.append(inicial[i])
        elif 'cc_' in inicial[i]:
            inicial[i] = inicial[i].replace('cc_', 'CC_')
            l_cc.append(inicial[i])
        elif 'ha_' in inicial[i]:
            inicial[i] = inicial[i].replace('ha_', 'HA_')
            l_ha.append(inicial[i])

    print(l_ha)
    print(l_cr)
    print(l_cc)        
