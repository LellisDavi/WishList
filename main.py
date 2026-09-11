from services.wishlist import Wishlist

def main():
    wishlist = Wishlist()
    wishlist.repositorio.criar_tabelas()

    while True:
        print('--- MENU WISHLIST --- ')
        print('[1] ADCIONAR CATEGORIA \n [2] ADICIONAR ITEM \n [3] LISTAR ITENS \n [4] MARCAR ITEM \n [5] LISTAR ADQUIRIDOS \n [6] SAIR')
if __name__ == '__main__':
    main()
