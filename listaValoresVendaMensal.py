def valores_venda_mensal(venda_mensal):
    total_renda = 0

    for elem in venda_mensal:
        total_renda += elem[1]
    percentual_renda = []
    for elem in venda_mensal:
        if (total_renda == 0):
            percentual_renda.append((elem[1], 0))
        else:
            percentual_renda.append((round(elem[1] / total_renda)))
    return percentual_renda