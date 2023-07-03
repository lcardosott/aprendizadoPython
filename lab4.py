func = 'x'
while func != '0':
    divisores = []
    if func == '+':
        result = int(base1) + int(base2)
        print (result)

    elif func == '-':
        result = int(base1) - int(base2)
        print (result)

    elif func == '*':
        result = int(base1) * int(base2)
        print(result)

    elif func == '/':
        div = int(base1) // int(base2)
        res = int(base1) % int(base2)
        print(div,res)

    elif func == ';':
        sub = abs(int(base1)-int(base2))
        if sub == 0:
            print ('0')
        else:
            for i in range (1, sub+1):
                divisor = sub%i

                if divisor == 0:
                    divisores.append (i)
            print (*divisores)

    base = (input())
    func,base1,base2 = base.split(' ')