##Querida Professora Carla:
##Quando eu escrevi esse código,
##apenas Deus e eu sabíamos como
##ele funcionava.
##Agora, apenas Deus sabe!

##Portanto, se você estiver
##tentando entender esta rotina porque
##estava falhando e "com certeza está"
##por favor, aumente este contador
##como um aviso para a proxima
##pessoa

##total_horas_gastas_aqui: 7

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