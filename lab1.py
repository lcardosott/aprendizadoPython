dia = int(input())
semana = input ()
valor = float(input())

if dia % 7 == 0:
    valor = valor*0.50

elif semana == "sexta-feira":
    if dia % 7 == 0:
        valor = valor*0.50
    
    else:
        valor = valor*0.75 

else:
    valor = valor-dia
    if valor <= 0:
        valor = 0

if semana == 'sábado' or semana == 'domingo':
    print (f'{valor:.2f}')
    print ('Agradecemos a preferência, tenha um ótimo fim de semana!')

elif semana == 'segunda-feira':
    print (f'{valor:.2f}')
    print ('É um dia terrível, você não devia ter saído da cama.')

else: 
    print (f'{valor:.2f}')
    print ('Agradecemos a preferência, tenha uma ótima ' , semana,'!', sep='')





