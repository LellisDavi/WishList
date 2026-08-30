from models.categoria import Categoria
class Item():
    def __init__(self, nome:str, preco: float, categoria:Categoria, status:str):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.status = status


    def obter_tipo(self):
       return self.categoria.tipo   
