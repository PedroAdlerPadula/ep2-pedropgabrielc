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
        else:
            dados_rolados2.append(dados_rolados[i])
    return lista_final

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    dados_no_estoque2 = []
    lista_final = [dados_rolados, dados_no_estoque2]
    for i in range(len(dados_no_estoque)):
        if i == dado_para_remover:
            dados_rolados.append(dados_no_estoque[i])
        else:
            dados_no_estoque2.append(dados_no_estoque[i])
    return lista_final

def calcula_pontos_regra_simples(dados_rolados):
    soma_face1 = 0
    soma_face2 = 0
    soma_face3 = 0
    soma_face4 = 0
    soma_face5 = 0
    soma_face6 = 0
    for i in range(1, 6):