import sqlite3


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
         
j