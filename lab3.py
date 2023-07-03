q = int(input ())
t = float(input ())
c = float(input ())
n = int(input ())
id = q
i = 1
vp = 0
value = 0
doses = 0

if q<=1000 and q>=1:
    while id>0:
        vi=t*i+t*c
        vp = vp+vi
        print (i,f'{vi:.2f}',f'{vp:.2f}')
        i+= 1
        id -=1
    
    print (f'{vp:.2f}')

    while value<=vp:
        value+= n
        if value<=vp:
            print (value)
            doses +=1
        else:
            continue
            
    print (doses, "\nBATERIA DE TESTES TERMINADA", sep='')