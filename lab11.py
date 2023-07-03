n = int(input())
leitores = 0
maior_leitores = ['',0]
maior_leitores_final = ['',0]
quantidade_cliques = 0
maior_tempo = 0
paragrafos_totais = 0

for i in range(n):
    arquivo = open(input(), 'r')
    nId = int(((arquivo.readline().split('nId: '))[1]).strip('\n'))
    titulo = (arquivo.readline().split('titulo: ')[1]).strip('\n')
    qtd_leitores = int((arquivo.readline().split('qtdLeitores: ')[1]).strip('\n'))
    qtd_leitores_final = int((arquivo.readline().split('qtdLeitoresFinal: ')[1]).strip('\n'))
    qtd_cliques = int((arquivo.readline().split('qtdCliques: ')[1]).strip('\n'))
    tempo = int((arquivo.readline().split('tempo: ')[1]).strip('\n'))

    paragrafos = 0
    for linha in arquivo:
        paragrafos += 1
    arquivo.close
    leitores += qtd_leitores

    if maior_leitores[1] < qtd_leitores:
        titulo_padronizado = '"' + titulo + '"'
        maior_leitores = [titulo_padronizado, qtd_leitores]

    if maior_leitores_final[1] < qtd_leitores_final:
        titulo_padronizado = '"' + titulo + '"'
        maior_leitores_final = [titulo_padronizado, qtd_leitores_final]

    quantidade_cliques += qtd_cliques

    if maior_tempo < tempo:
        maior_tempo = tempo

    paragrafos_totais += paragrafos
    nome = 'relatorio_' + str(nId) + '.txt'
    relatorio = open( nome , 'w')
    relatorio.write('nId: ' + str(nId))
    relatorio.write('\nqtdLeitores: ' + str(qtd_leitores)) 
    relatorio.write('\nqtdLeitoresFinal: ' + str(qtd_leitores_final))
    relatorio.write('\nqtdCliques: ' + str(qtd_cliques))
    relatorio.write('\ntempo: ' + str(tempo))
    relatorio.close

final = open ('relatorio_final.txt', 'w')
final.write(str(leitores//n) + '\n')
final.write(maior_leitores[0] + ' '+ str(maior_leitores[1]) + '\n')
final.write(maior_leitores_final[0] + ' ' + str(maior_leitores_final[1]) + '\n')
final.write(str(quantidade_cliques//n) + '\n')
final.write(str(maior_tempo) + '\n')
final.write(str(paragrafos_totais//n))
final.close