import sqlite3
from unittest import TestCase
import sys
from ConexaoDB import conectar, desconectar
sys.path.insert(0, '..')
BD = "TestBD.db"
class MockBD(TestCase):
    @classmethod
    def setUpClass(cls):
        con = conectar(BD)
        cursor = con.cursor()
        query_criar_tabela_usuario = """CREATE TABLE Usuario (id int NOT NULL PRIMARY KEY, nome text NOT NULL, endereco text NOT NULL, tipo_usuario text NOT NULL)"""
        query_criar_tabela_produtos = """CREATE TABLE Produtos (id int NOT NULL PRIMARY KEY , nome text NOT NULL, cod int, categoria text NOT NULL, preco float NOT NULL, quantidade int)"""
        query_criar_tabela_venda = """CREATE TABLE Venda (id int NOT NULL PRIMARY KEY , id_responsavel int NOT NULL FOREIGN KEY, total float NOT NULL)"""
        query_criar_tabela_produto_venda = """CREATE TABLE Produto_venda (id int NOT NULL PRIMARY KEY , id_venda int NOT NULL FOREIGN KEY, quantidade int NOT NULL)"""

        try:
            cursor.execute(query_criar_tabela_usuario)
            cursor.execute(query_criar_tabela_produtos)
            cursor.execute(query_criar_tabela_venda)
            cursor.execute(query_criar_tabela_produto_venda)
            con.commit()
        except sqlite3.Error as error:
            print("Erro na criação das tabelas:", error)
        else:
            print("Criação das tabelas: OK")
            query_inserir_usuario = """INSERT INTO Usuario (id, nome, endereco, tipo_usuario) VALUES
            (1, 'Carla F.', 'rua', 'cliente'),
            (2, 'Danilo', 'rua', 'admin'),
            (3, 'Daniel', 'rua', 'vendedor'),
            (4, 'Alice', 'rua', 'vendedor')"""
            query_inserir_produtos = """INSERT INTO Produtos (id, nome, cod, categoria, preco, quantidade) VALUES
            (1, 'detergente', '1', 'limpeza', '20', '5'),
            (2, 'leite', '2','laticios', '5', '2'),
            (3, 'sabao', '3', 'limpeza', '7.50', '5'),
            (4, 'pasta de dente', '4', 'higiene', '3', '20')"""
            query_inserir_vendas = """INSERT INTO Venda (id, id_responsavel, total) VALUES
            ('1', '3', '5'),
            ('1', '4', '5')"""
            query_inserir_produto_venda = """INSERT INTO Produto_venda (id, id_responsavel, total) VALUES
            ('1', '3', '5'),
            ('1', '4', '5')"""
            try:
                cursor.execute(query_inserir_usuario)
                cursor.execute(query_inserir_produtos)
                cursor.execute(query_inserir_vendas)
                cursor.execute(query_inserir_produto_venda)
                con.commit()
            except sqlite3.Error as error:
                print("Erro na criação das tabelas:", error)

    @classmethod
    def tearDownClass(cls):
        print("TearDown")
        con = conectar(BD)
        cursor = con.cursor()
        try:
            cursor.execute("DROP TABLE Usuario")
            cursor.execute("DROP TABLE Produtos")
            cursor.execute("DROP TABLE Vendas")
            cursor.execute("DROP TABLE Produto_vendas")
            con.commit()
            cursor.close()
            print("Removeu os dados das tabelas.")
        except sqlite3.Error as error:
            print("Banco de dados não existe. Erro na remoção do BD.", error)
        finally:
            desconectar(con)
