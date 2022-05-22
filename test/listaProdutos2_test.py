from listaProdutos2 import *
import unittest

class test_procentagem_produtos(unittest.TestCase):
    def porcentagem(self):
        venda =  [(1, 1, 4), (1, 2, 3), (1, 3, 1), (2, 1, 3)]
        self.assertEqual(test_procentagem_produtos(1, 0.6365))
        self.assertEqual(test_procentagem_produtos(2, 0.2727))
        self.assertEqual(test_procentagem_produtos(3, 0.0909))
        self.assertEqual(test_procentagem_produtos(4, 0))