import random
def rolar_dados(numero):
    lista_final = []
    for i in range(numero):
        num = random.randint(1, 6)
        lista_final.append(num)
    return lista_final
