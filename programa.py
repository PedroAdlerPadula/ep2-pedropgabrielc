from funcoes import *

armazena_pontos  = {
    'regra_simples': {
        1: -1,
        2: -1,
        3: -1,
        4: -1,
        5: -1, 
        6: -1,
    },
    'regra_avancada' : {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1,
        
    }
}

contagem = 0 

imprime_cartela(armazena_pontos)

while contagem < 12: 
    dados = rolar_dados(5)
    dados_guardados = []
    jogando = True 
    rolar_novamente = 0 
    while jogando:
        print("Dados rolados: {}".format(dados))
        print("Dados guardados: {}".format(dados_guardados))
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        entrada = input(">")

        while entrada != "0" and entrada != "1" and entrada != "2" and entrada != "3" and entrada != "4":
            print("Opção inválida. Tente novamente.")
            entrada = input(">")

        if entrada == "0":
            print("Digite a combinação desejada:")
            while jogando:
                combinacao = input(">")

                if combinacao == "1" or combinacao == "2" or combinacao == "3" or combinacao == "4" or combinacao == "5"or combinacao == "6":
                    if armazena_pontos["regra_simples"][int(combinacao)] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        lista_jogada = dados_guardados + dados
                        armazena_pontos = faz_jogada(lista_jogada, combinacao, armazena_pontos)
                        jogando = False
                elif combinacao == "sem_combinacao" or combinacao == "quadra" or combinacao == "full_house" or combinacao == "sequencia_baixa" or combinacao == "sequencia_alta" or combinacao == "cinco_iguais":
                    if armazena_pontos["regra_avancada"][combinacao] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        lista_jogada = dados_guardados + dados
                        armazena_pontos = faz_jogada(lista_jogada, combinacao, armazena_pontos)
                        jogando = False
                else:
                    print("Combinação inválida. Tente novamente.")

        elif entrada == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            g = int(input(">"))
            if g < len(dados):
                lista = guardar_dado(dados, dados_guardados, g)
                dados = lista[0]
                dados_guardados = lista[1]

        elif entrada == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            r = int(input(">"))
            if r < len(dados_guardados):
                lista = remover_dado(dados, dados_guardados, r)
                dados = lista[0]
                dados_guardados = lista[1]

        elif entrada == "3":
            if rolar_novamente >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                dados = rolar_dados(len(dados))
                rolar_novamente += 1

        elif entrada == "4":
            imprime_cartela(armazena_pontos)

    if -1 not in armazena_pontos["regra_simples"].values() and  -1 not in armazena_pontos["regra_avancada"].values():
        break


    contagem += 1

soma_regra_simples = 0
for valor in armazena_pontos['regra_simples'].values():
    if valor != -1:
        soma_regra_simples += valor

soma_regra_avancada = 0
for valor in armazena_pontos['regra_avancada'].values():
    if valor != -1:
        soma_regra_avancada += valor

valor_total = soma_regra_simples + soma_regra_avancada

if soma_regra_simples >= 63:
    valor_total += 35
imprime_cartela(armazena_pontos)
print("Pontuação total: {}".format(valor_total))
