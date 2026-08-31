from models.categoria import Categoria
from models.item import Item
from repositorio import Repositorio

def main():
    saude=Categoria('saude','necessidade')
    item1=Item('Escova de Dente', 20, categoria=saude,status='pendente') 
    print(item1.obter_tipo())

    
if __name__ == '__main__':
    main()
