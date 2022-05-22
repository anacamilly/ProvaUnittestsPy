from listaValoresVendaMensal import *
import unittest
class test_total_produtos(unittest.TestCase):
    def test_percentual_lista_produtos(self):
        venda_mensal = [('1/22', 400.50), ('2/22', 1000.00), ('3/22', 10.50), ('4/22', 100.30)]

        situacao1 = [('1/22', 400.50), ('2/22', 1000.00)]
        r_esperado1 = 149.0
        situacao2 = [('2/22', 1000.00), ('3/22', 10.50)]
        r_esperado2 = -98.95

        self.assertEqual(valores_venda_mensal(situacao1), r_esperado1)
        self.assertEqual(valores_venda_mensal(situacao2), r_esperado2)