import random
def rolar_dados(numero):
    lista_final = []
    for i in range(numero):
        num = random.randint(1, 6)
        lista_final.append(num)
    return lista_final

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    dados_rolados2 = []
    lista_final = [dados_rolados2, dados_no_estoque]
    for i in range(len(dados_rolados)):
        if i == dado_para_guardar:
            dados_no_estoque.append(dados_rolados[i])
            dados_rolados[i] not in dados_rolados
        else:
            dados_rolados2.append(dados_rolados[i])
    return lista_final