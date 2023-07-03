from os import sep
age = int(input())
defalut_answer = ('*Que página de meme do Instagram você é?*')
idade = ('\nQual a sua idade?')
error = ('Erro: entrada inválida')
question1 = ('Quantos segundos são necessários para saber se um vídeo é bom?')
question2 = ('Qual banda você gosta mais?')
question3 = ('São as capivaras os melhores animais da Terra?')
question4 = ('Que imagem de bom dia você manda no grupo da família?')
answer = ('Sua página de memes é: ')
#-------------------------------------------------------
if age<25 and age>=0:
    time = int(input())
    if time<=5 and time>0:
        print (defalut_answer,idade,'\n',age,'\n',question1,'\n',time,'\nRESULTADO\n','Você deveria estar no TikTok',sep='')
    elif time>5:
        print (defalut_answer,idade,'\n',age,'\n',question1,'\n',time,'\nRESULTADO\n',answer,'@meltmemes',sep='')
    else:
        print (defalut_answer,idade,'\n',age,'\n',question1,'\n',time,'\n',error,sep='')
#-------------------------------------------------------
elif age>=25 and age<=40:
    band = input()
    if band == ('A'):
        print (defalut_answer,idade,'\n', age,'\n', question2,'\n', band,') Matanza\nRESULTADO\n', answer,'@badrockistamemes',sep='')

    elif band == ('B'):
        print (defalut_answer,idade,'\n', age,'\n', question2,'\n', band,') Iron Maiden\nRESULTADO\n', answer,'@badrockistamemes',sep='')

    elif band == ('C'):
        capivara= input()
        if capivara == ('Sim'):
            print (defalut_answer,idade,'\n', age,'\n', question2,'\n', band,") Imagine Dragons",'\n',question3,'\n',capivara,'\nRESULTADO\n', answer,'@genteboamemes',sep='')
        elif capivara == ('Não'):
            print (defalut_answer,idade,'\n', age,'\n', question2,'\n', band,") Imagine Dragons",'\n',question3,'\n',capivara,'\nRESULTADO\n',answer,'@wrongchoicememes')
        else:
            print (defalut_answer,idade,'\n', age,'\n', question2,'\n', band,") Imagine Dragons",'\n',question3,'\n',capivara,'\n', error,sep='')

    elif band == ('D'):
        capivara= input()
        if capivara == ('Sim'):
            print (defalut_answer,idade,'\n', age,'\n', question2,'\n', band,') BlackPink','\n',question3,'\n',capivara,'\nRESULTADO\n', answer,'@genteboamemes',sep='')
        elif capivara == ('Não'):
            print (defalut_answer,idade,'\n', age,'\n', question2,'\n', band,') BlackPink','\n',question3,'\n',capivara,'\nRESULTADO\n',answer,'@wrongchoicememes',sep='')
        else:
            print (defalut_answer,idade,'\n', age,'\n', question2,'\n', band,') BlackPink','\n',question3,'\n',capivara,'\n', error,sep='')
    else:
        print (defalut_answer,idade,'\n', age,'\n', question2,'\n', band,"\n",error,sep='')
#-------------------------------------------------------
elif age>40 and age<=125:
    image = input()
    if image ==('A'):
       print(defalut_answer,idade,'\n', age,'\n', question4,'\n', image,') Bebê em roupa de flor','\nRESULTADO\n', answer,'@bomdiabebe',sep='')
    elif image == ('B'):
        print(defalut_answer,idade,'\n', age,'\n', question4,'\n', image,') Gato','\nRESULTADO\n', answer,'@kittykatmsgs',sep='')
    elif image == ('C'):
        print(defalut_answer,idade,'\n', age,'\n', question4,'\n', image,') Coração e rosas','\nRESULTADO\n', answer,'@bomdiaflordodia',sep='')
    else:
        print (defalut_answer,idade,'\n', age,'\n', question4,'\n', image,'\n',error,sep='')
#-------------------------------------------------------
else: print (defalut_answer,idade,'\n',age,'\n',error,sep='')