lifeS, atkS, defS = map(int, input().split())
lifeC, atkC, defC = map(int, input().split())
seed = int(input())
turn = 0
sarah = 'Sarah'
clone = 'O clone'

def random(x, i):
    global seed
    seed = (7 * x + 111)% 1024
    number = seed % i
    print ('MENSAGEM DEBUG - número gerado:', seed)
    return number

def punch(atkA ,defO ,player):
    damage = (atkA-defO) * random(seed,3)
    if damage >= 0:
        print (player, 'sofreu', damage,'pontos de dano!')
    else:
        print (player, 'sofreu', 0,'pontos de dano!')
        damage = 0
    return damage 

def knife(atkA, player):
    n = random (seed,6)
    total_damage=0
    for i in range (1, n+1):
        damage = atkA//(3**i)
        total_damage += damage
    if total_damage >= 0:
        print (player, 'sofreu', total_damage,'pontos de dano!')
    else:
        total_damage = 0
        print (player, 'sofreu', 0,'pontos de dano!')
    return total_damage

def summon_fairy (player):
    p = random (seed, 100)
    q = random (seed, 1024)
    print (player, 'ganhou', p, 'pontos de vida!')
    if q % 2 != 0 and q < 100:
        print (player, 'ganhou', q, 'pontos de ataque!')
        return p, q, False
    elif q % 2 == 0 and q < 100:
        print (player, 'ganhou', q, 'pontos de defesa!')
        return p, q, False
    elif q >= 1019:
        return p, q, True
    else:
        return p, q, False
        
def lifes(sarah,clone):
    if sarah <= 0:
        print ('Sarah foi derrotada...')
        return False
    elif clone <= 0:
        print ('O clone foi derrotado! Sarah venceu!\nFIM - PARABENS')
        return False
    else:
        return True

while lifeS > 0 and lifeC > 0:
    function = input()
    if turn % 2 == 0:
        if function == 'soco':
            damage = punch(atkS, defC, clone)
            lifeC -= damage
            lifes (lifeS,lifeC)

        elif function == 'facas':
            damage = knife (atkS, clone)
            lifeC -= damage
            lifes (lifeS,lifeC)

        else:
            p, q, monster = summon_fairy (sarah)
            lifeS += p
            if monster:
                print ('O quê? A fada trouxe um monstro gigante com ela!\nO Clone e o castelo foram destruídos,\ne Sarah agora tem um novo pet.\nFINAL SECRETO - PARABENS???')
                lifeC = 0

            elif q % 2 != 0 and q < 100:
                atkS += q

            elif q % 2 == 0 and q < 100:
                defS += q

    else: 
        if function == 'soco':
            damage = punch(atkC, defS, sarah)
            lifeS -= damage
            lifes (lifeS,lifeC)

        elif function == 'facas':
            damage = knife (atkC, sarah)
            lifeS -= damage
            lifes (lifeS,lifeC)

        else:
            p, q, monster = summon_fairy (clone)
            lifeC += p
            if monster:
                print ('O quê? A fada trouxe um monstro gigante com ela!\nSarah foi derrotada...')
                lifeS = 0

            elif q % 2 != 0 and q < 100:
                atkC += q

            elif q % 2 == 0 and q < 100:
                defC += q
    turn += 1
