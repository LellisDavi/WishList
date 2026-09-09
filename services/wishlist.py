from repositorio.repositorio import Repositorio
from models.categoria import Categoria
from models.item import Item


class Wishlist():
    def __init__(self):
        self.repositorio = Repositorio()


    def adicionar_categoria(self,nome,tipo):
        categorias_existentes = self.repositorio.buscar_categoria()
        for l in categorias_existentes:
            if nome.lower() == l.nome.lower():
                return f"Essa categoria já existe."
        nova_categoria = Categoria(nome, tipo)
        self.repositorio.inserir_categoria(nova_categoria)    
            
            

