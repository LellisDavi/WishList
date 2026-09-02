import sqlite3
from models.categoria import Categoria
from models.item import Item

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


    def buscar_itens(self):
        self.cursor.execute("SELECT item.id, item.nome, item.preco, item.status, categoria.id, categoria.nome, categoria.tipo FROM item JOIN categoria ON item.categoria_id = categoria.id")
        linhas = self.cursor.fetchall()
        lista = []
        for l in linhas:
            id_categoria = l[4] 
            nome_categoria = l[5]     
            tipo_categoria = l[6]
            categoria_item=Categoria(nome_categoria,tipo_categoria,id_categoria)

            id_item = l[0]
            nome_item = l[1]
            preco_item = l[2]
            status_item = l[3] 
            item_buscado =Item(nome=nome_item,preco=preco_item,categoria=categoria_item,status=status_item,id=id_item )
            lista.append(item_buscado)
        return lista


    def atualizar_status(self, id_item, novo_status):
        self.cursor.execute("UPDATE item SET status = ? WHERE id = ?", (novo_status, id_item))
        self.banco.commit()
        
            