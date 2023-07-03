class salas:
    """ Esta classe tem a finalidade de armazenar os dados das diferentes salas presentes em 
nosso mapa, atribuindo caracteristicas como número da sala, portas adjascentes e itens.
    No caso dos itens, com o auxílio do @property e @item.setter, somos capazes de alterar os valores
deste atributo.
    """
    def __init__ (self, numero, adjascentes1, adjascentes2, adjascentes3, adjascentes4, item='vazia'):
        self.numero = numero
        self.adjascentes1 = adjascentes1
        self.adjascentes2 = adjascentes2
        self.adjascentes3 = adjascentes3
        self.adjascentes4 = adjascentes4
        self.item = item

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, item):
        self._item = item

qtdd_sala = int(input())
l_sala = []
for i in range (qtdd_sala):
    numero, adjascentes1, adjascentes2, adjascentes3, adjascentes4 = input().split(' ')
    sala = salas(numero, adjascentes1, adjascentes2, adjascentes3, adjascentes4)
    l_sala.append(sala)

qtdd_item = int(input())
l_item = []
for i in range (qtdd_item):
    sala_item, nome_item = input().split()
    sala_item = int(sala_item)
    l_sala[sala_item].item = nome_item

sala_clone = int(input())
sala_atual = int(input())
tam_inventario = int(input())
comandos = input().split()
int_comandos = list(map(int,comandos))
l_inventario = []
vida_bot = True
aux = 0
#----------------------------------------
print ('Bem-vindo as Aventuras de Sarah 2.0\n'
    'Sarah acorda no saguão do antigo castelo de sua família,ela tem a oportunidade única de derrotar o seu clone maligno que se apoderou do reino.\n'
    'Para isso ela deve encontrar o baú da sua família que contém a espada mágica que apenas a verdadeira herdeira pode utilizar.\n'
    'Na sala onde está Sarah vê várias portas. Qual é a sua próxima ação?\n'
    'DEBUG - O clone está na sala:', sala_clone)
#----------------------------------------    
while sala_atual != sala_clone and vida_bot:
    
    relacao = [l_sala[sala_atual].adjascentes1, l_sala[sala_atual].adjascentes2,l_sala[sala_atual].adjascentes3, l_sala[sala_atual].adjascentes4]
    relacao_portas = list(map(int,relacao))
    if l_sala[sala_atual].item == 'vazia':
        print ('Você está na sala de número', sala_atual ,'e dela você pode ir para as salas', relacao_portas)

    else:
        print ('Você está na sala de número', sala_atual, 'ela contém um baú com', l_sala[sala_atual].item, 'e dela você pode ir para as salas', relacao_portas)
        print ('Pegar', l_sala[sala_atual].item)        
        if len(l_inventario) < tam_inventario:
            l_inventario.append(l_sala[sala_atual].item)
            print (l_sala[sala_atual].item, 'adicionado ao inventário')
            l_sala[sala_atual].item = 'vazia'
            if 'poção' in l_inventario:
                print ('Você pegou a poção da morte e virou pó instantaneamente. Tente novamente...')
                vida_bot = False
        else:
            print ('Inventário cheio!')
            
    if aux < len(int_comandos):
        sala_atual = int_comandos[aux]
        print ('Mover para sala', sala_atual)
        aux += 1

if vida_bot:
    if 'espada' in l_inventario:
        print ('Você derrotou o clone maligno com a espada mágica! Com a Sarah no reino o mundo pode voltar ao equilíbrio.\n'
        'PARABÉNS!')
    else:
        print ('Infelizmente você encontrou o clone sem a espada das fadas e foi derrotado. Tente novamente...')
