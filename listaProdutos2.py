def percentual_produtos(listProdut):
    total_renda = 0
    for elem in listProdut:
        total_renda += elem[1]
    percentual_renda = []
    for elem in listProdut:
        if (total_renda == 0):
            percentual_renda.append((elem[0], 0))
        else:
            percentual_renda.append((elem[0], round(elem[1] / total_renda, 4)))
        return percentual_renda


def percentual_renda_media(lista):
    qnt_fontes_renda = len(lista[0])

    lista_media = []
    for trabalho in range(qnt_fontes_renda):
        valor_total_mes = 0
        for mes in lista:
            valor_total_mes += mes[trabalho][1]
        lista_media.append((lista[0][trabalho][0], valor_total_mes))

    return percentual_produtos(lista_media)