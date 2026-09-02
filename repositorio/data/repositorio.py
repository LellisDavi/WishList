import sqlite3
from models.categoria import Categoria

class Repositorio():
    def __init__(self):
        self.banco = sqlite3.connect('database/wishlist.db')
        self.cursor = self.banco.cursor()

    def criar_tabelas(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS categoria (" \
        "id integer PRIMARY KEY AUTOINCREMENT," \
        " nome text," \
        " tipo text)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS item (" \
        "id integer PRIMARY KEY AUTOINCREMENT," \
        " nome text," \
        " preco double," \
        " categoria_id integer," \
        " status text," \
        " FOREIGN KEY (categoria_id) REFERENCES categoria(id))")
        self.banco.commit()

    def fechar_conexao(self):
        self.banco.close()    


    def inserir_categoria(self,categoria):
        self.cursor.execute("INSERT INTO categoria(nome, tipo) VALUES (?,?)", (categoria.nome, categoria.tipo)) 
        novo_id = self.cursor.lastrowid
        self.banco.commit()
        return novo_id

    def inserir_item(self, item, categoria_id):
        self.cursor.execute("INSERT INTO item(nome,preco,categoria_id, status) VALUES (?,?,?,?)",(item.nome, item.preco, categoria_id, item.status))
        novo_id_item = self.cursor.lastrowid
        self.banco.commit()
        return novo_id_item

    def buscar_categoria(self):
        self.cursor.execute("SELECT * FROM categoria") 
        linhas = self.cursor.fetchall()
        lista = []
        for l in linhas:
            id = l[0]
            nome = l[1]
            tipo = l[2]
            categoria_buscada=Categoria(nome, tipo, id)
            lista.append(categoria_buscada)
        return lista    


        
            