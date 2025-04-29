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
    dicio_final = {}
    soma_face1 = 0
    soma_face2 = 0
    soma_face3 = 0
    soma_face4 = 0
    soma_face5 = 0
    soma_face6 = 0
    for i in range(len(dados_rolados)):
        if dados_rolados[i] == 1:
            soma_face1 +=1
        if dados_rolados[i] == 2:
            soma_face2 +=2
        if dados_rolados[i] == 3:
            soma_face3 +=3
        if dados_rolados[i] == 4:
            soma_face4 +=4
        if dados_rolados[i] == 5:
            soma_face5 +=5
        if dados_rolados[i] == 6:
            soma_face6 +=6
    dicio_final[1] = soma_face1
    dicio_final[2] = soma_face2
    dicio_final[3] = soma_face3
    dicio_final[4] = soma_face4
    dicio_final[5] = soma_face5
    dicio_final[6] = soma_face6

    return dicio_final

def calcula_pontos_soma(dados_rolados):
    soma_final = 0
    for i in range(len(dados_rolados)):
        soma_final += dados_rolados[i]
    return soma_final