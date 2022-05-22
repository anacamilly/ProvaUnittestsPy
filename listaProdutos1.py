def quant_produtos(listProd):
    if(len(listProd)<=5):
        return 1
    resultado = 1
    quant_produtos = listProd [0] [1]
    for elem in quant_produtos:
        if(elem[1] == quant_produtos):
            resultado.append((elem))
        elif(elem[1] > quant_produtos):
            quant_produtos = elem[1]
            resultado = []
            resultado.append(elem)
    return resultado