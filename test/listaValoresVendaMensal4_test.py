from listaValoresVendaMensal import *
import unittest

class test_total_produtos(unittest.TestCase):
    def test_melhoria_vendas_produtos(self):
        situacao1 = [('1/22', 400.50), ('2/22', 1000.00), ('3/22', 10.50), ('4/22', 10.50)]

        self.assertEqual(melhoria_vendas('1/22', situacao1), False)
        self.assertEqual(melhoria_vendas('2/22', situacao1), 1.4969)
        self.assertEqual(melhoria_vendas('3/22', situacao1), -0.9895)
        self.assertEqual(melhoria_vendas('4/22', situacao1), 0)
