species = int(input())
dRelation , dFeatures = {}, {}
for i in range(species):
    tag, features = input().split(' | ')
    dRelation[tag] = features.split()

qttfeatures = int(input())
for i in range(qttfeatures):
    if i == 0:
        primitive = input()
        feature = primitive
    else:
        feature = input()
    dna1, dna2 = input(), input()
    listdna1, listdna2 = list(dna1),list(dna2)
    listaux = []
    for i in range(len(dna1)):
        listaux.append(listdna1[i]+listdna2[i])
    listaux.append(0) #este último valor de 'listaux', servirá para pontuar a quantidade de mutações em relação ao primitivo  
    dFeatures[feature] = listaux

for i in dFeatures:
    if i != primitive:
        for j in range(len(dFeatures[i])-1): #'-1 é retirado pois o último elemento da lista se refere a quantidade'
            if (dFeatures[primitive])[j] < (dFeatures[i])[j]:
                dFeatures[i][-1] += 1
        dFeatures[i]=dFeatures[i][-1]
dFeatures[primitive] = 0

rank = []
for i in sorted(dFeatures, key = dFeatures.get):
    rank.append(i)
rankdecre = list(reversed(rank))
listRelation = [*dRelation]
for i in rankdecre:
    for j in listRelation:
        if i in dRelation[j] and type(dRelation[j]) == list:
            dRelation[j] = i

for i in rank:
    print ('CARACTERÍSTICA:', i)
    for j in listRelation:
        if i == dRelation[j]:
            print (j)
