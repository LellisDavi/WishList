from repositorio.repositorio import Repositorio
from models.categoria import Categoria
from models.item import Item


class Wishlist():
    def __init__(self):
        self.repositorio = Repositorio()


    def adicionar_categoria(self,nome,tipo):
        categorias_existentes = self.repositorio.buscar_categoria()
        for categoria in categorias_existentes():
            if nome == categorias_existentes.nome:
