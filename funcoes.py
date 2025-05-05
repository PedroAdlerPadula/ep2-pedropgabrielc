# ex 1
import random
def rolar_dados(numero):
    lista_final = []
    for i in range(numero):
        num = random.randint(1, 6)
        lista_final.append(num)
    return lista_final

#ex 2
def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    dados_rolados2 = []
    lista_final = [dados_rolados2, dados_no_estoque]
    for i in range(len(dados_rolados)):
        if i == dado_para_guardar:
            dados_no_estoque.append(dados_rolados[i])
        else:
            dados_rolados2.append(dados_rolados[i])
    return lista_final

#ex 3
def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    dados_no_estoque2 = []
    lista_final = [dados_rolados, dados_no_estoque2]
    for i in range(len(dados_no_estoque)):
        if i == dado_para_remover:
            dados_rolados.append(dados_no_estoque[i])
        else:
            dados_no_estoque2.append(dados_no_estoque[i])
    return lista_final

#ex 4
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

#ex 5
def calcula_pontos_soma(dados_rolados):
    soma_final = 0
    for i in range(len(dados_rolados)):
        soma_final += dados_rolados[i]
    return soma_final

#ex 6
def calcula_pontos_sequencia_baixa(dados_rolados):
    if 1 in dados_rolados and 2 in dados_rolados and 3 in dados_rolados and 4 in dados_rolados:
        return 15
    elif 2 in dados_rolados and 3 in dados_rolados and 4 in dados_rolados and 5 in dados_rolados:
        return 15
    elif 3 in dados_rolados and 4 in dados_rolados and 5 in dados_rolados and 6 in dados_rolados:
        return 15
    else:
        return 0

#ex 7
def calcula_pontos_sequencia_alta(dados_rolados):
    if 1 in dados_rolados and 2 in dados_rolados and 3 in dados_rolados and 4 in dados_rolados and 5 in dados_rolados:
        return 30
    elif 2 in dados_rolados and 3 in dados_rolados and 4 in dados_rolados and 5 in dados_rolados and 6 in dados_rolados:
        return 30
    else:
        return 0
#ex 8 
def calcula_pontos_full_house(dados_rolados):
    lista1 = [dados_rolados[0]]
    lista2 = []
    soma = 0
    for i in range(len(dados_rolados)):
        soma += dados_rolados[i]
    for i in range(1,len(dados_rolados)):
        if dados_rolados[i] not in lista1:
            lista2.append(dados_rolados[i])
        elif dados_rolados[i] in lista1:
            lista1.append(dados_rolados[i])
        elif dados_rolados[i] in lista2:
            lista2.append(dados_rolados[i])
    if len(lista1) == 3 and len(lista2) == 2:
        if lista2[0] == lista2[1]:
            return soma
    if len(lista1) == 2 and len(lista2) == 3:
        if lista2[0] == lista2[1] == lista2[2]:
            return soma
    return 0

#ex 9
def calcula_pontos_quadra(lista_faces):
    dicio = {}
    soma = 0
    contagem = 0 
    for i in range(len(lista_faces)):
        soma += lista_faces[i]

    for i in lista_faces:
        if i in dicio:
            dicio[i] += 1
        else:
            dicio[i] = 1

    for k in dicio.values():
        if k >= 4:
            return soma
    else:
        return 0
    
#ex 10
def calcula_pontos_quina(lista_valores):
    dicio = {}
    for i in lista_valores:
        if i in dicio:
            dicio[i] += 1
        else:
            dicio[i] = 1

    for k in dicio.values():
        if k >= 5:
            return 50
    else:
        return 0

#ex 11 
def calcula_pontos_regra_avancada(valores):
    sem_comb = calcula_pontos_soma(valores)
    seq_baixa = calcula_pontos_sequencia_baixa(valores)
    seq_alta = calcula_pontos_sequencia_alta(valores)
    full_house = calcula_pontos_full_house(valores)
    quadra = calcula_pontos_quadra(valores)
    cinco_iguais = calcula_pontos_quina(valores)

    dicio_final = {
    'cinco_iguais': cinco_iguais,
    'full_house': full_house,
    'quadra': quadra,
    'sem_combinacao': sem_comb,
    'sequencia_alta': seq_alta,
    'sequencia_baixa': seq_baixa
}
    return dicio_final

# ex 12
def faz_jogada(dados, categoria, cartela):
    if categoria in ['1', '2', '3', '4', '5', '6']:
        pontos_por_numero = calcula_pontos_regra_simples(dados)
        cartela['regra_simples'][int(categoria)] = pontos_por_numero[int(categoria)]
    else:
        pontos_avancados = calcula_pontos_regra_avancada(dados)
        cartela['regra_avancada'][categoria] = pontos_avancados[categoria]
    
    return cartela

# funcção ex 13 
def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)

