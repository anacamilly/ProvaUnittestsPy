from ConexaoDB import *
def buscarProdutos(bd):
    return ler_bd(bd, "SELECT * FROM Produtos where  nome = ?")
