from listaProdutos3 import *
import unittest
class test_total_produtos(unittest.TestCase):
    def test_total_arrecadado(self):
        venda = ((1, 50.50), (2, 200.95), (3, 20.95), (4, 100.40)) #372.80

        r_esperado = (372.79999999999995)
        self.assertEqual(soma_produtos(venda), r_esperado)