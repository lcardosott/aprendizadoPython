from decimal import getcontext, Decimal
from recipes_decimal import pi
getcontext().prec = 36

def anos_luz(a, b, c, d, x):
    ''' A função retorna o valor de anos-luz de distância que uma determinada quantidade de combustível percorre
    '''
    return (pi()+(a*(Decimal(x).exp()))-(zeta(b, x)))/((Decimal(-(c*x)**Decimal(1/2)).exp()) + d*(2*(pi()**3)-x))

def zeta(b, x):
    ''' A função retorna o valor de zeta (no programa prinipal ela é acessada pela função 'anos-luz') 
    '''
    aux = 0
    s = (b*x) + pi()
    for i in range(1, 101):
        aux += 1/(i**s)
    return aux

def busca_binaria(a, b, c, d, d_planetas, maior):
    ''' A função realiza uma busca binária, a fim de encontrar o 'x'(quantidade de combustível)
    que chega mais próximo de 'y'(anos luz)
    '''
    y_final =  anos_luz(a, b, c, d, Decimal(25.))
    min, x,  max = 0, Decimal(25.), 50
    erro = Decimal(10**-32)* d_planetas[maior]
    while abs(y_final - d_planetas[maior]) > erro:
        if y_final > d_planetas[maior]:
            max = x
            x = (x + min)/2

        else:
            min = x
            x = (x + max)/2       
        y_final = anos_luz(a, b, c, d, x)
    return x    

def main():
    qtdd_rotas = int(input())
    while qtdd_rotas != 0:

        d_planetas = {}
        for i in range(qtdd_rotas):
            nome_planeta = input()
            d_planetas[nome_planeta] = Decimal(input())
        a = Decimal(input())
        b = Decimal(input())
        c = Decimal(input())
        d = Decimal(input())

        maior_distancia = anos_luz(a, b, c, d, Decimal(50.))
        maior = ''
        for i in sorted(d_planetas, key = d_planetas.get, reverse = True): #analisa (da maior distancia para a menor)
            if d_planetas[i] < maior_distancia:                            #se for possível realizar o salto, sai do loop e parte para a impressão
                maior = i
                break

        if maior == '':
            print ('GRAU~~')
        else: 
            print(maior)
            print(f"{busca_binaria(a, b, c, d, d_planetas, maior):.28f}")

        qtdd_rotas = int(input()) 

if __name__ == '__main__':
    main() 