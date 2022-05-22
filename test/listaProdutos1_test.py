from listaProdutos1 import *
import unittest
class test_quant_produtos(unittest.TestCase):
    def test_quant_produtos(self):
        produto = [('shampoo', 10), ('condicionador', 5), ('sabonete', 2)]
        self.assertEqual(quant_produtos(produto), 1)
        q