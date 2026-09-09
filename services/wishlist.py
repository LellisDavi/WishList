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


    def adicionar_item(self, nome_item, preco, nome_categoria, status):
        categoria_encontrada = None
        categorias_existentes = self.repositorio.buscar_categoria()
        for l in categorias_existentes:
            if nome_categoria.lower() == l.nome.lower():
                categoria_encontrada = l
            else:
                return "Categoria não encontrada, cadastre-a primeiro!"    
        if categoria_encontrada is not None:
            novo_item = Item(nome_item, preco, categoria_encontrada, status)
            self.repositorio.inserir_item(novo_item, categoria_encontrada.id)


    def listar_itens(self):
        itens = self.repositorio.buscar_itens()
        necessidades = list()
        desejos = list()
        for item in itens:
            if item.obter_tipo() == 'Necessidade':
                necessidades.append(item)
            else:
                desejos.append(item)
        print('=== Necessidades ===')
        for produto_necessidade in necessidades:
            print(f"Nome:{produto_necessidade.nome} Preço:{produto_necessidade.preco} Status:{produto_necessidade.status}")
        print('=== Desejos ===')
        for produto_desejo in desejos:
            print(f"Nome:{produto_desejo.nome} Preço:{produto_desejo.preco} Status:{produto_desejo.status}")  


    def marcar_como_adquirido(self, id):
        self.repositorio.atualizar_status(id, novo_status='adquirido')

















