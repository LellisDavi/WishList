from services.wishlist import Wishlist

def main():
    wishlist = Wishlist()
    wishlist.repositorio.criar_tabelas()

    while True:
        print('--- MENU WISHLIST --- ')
        print(''
        ' [1] ADICIONAR CATEGORIA ' \
        '\n [2] LISTAR CATEGORIA ' \
        '\n [3] ADICIONAR ITEM ' \
        '\n [4] LISTAR ITENS ' \
        '\n [5] MARCAR ITEM ' \
        '\n [6] LISTAR ADQUIRIDOS ' \
        '\n [7] SAIR')

        escolha = int(input('Digite sua opção: '))
        if escolha == 1:
            nome = input('Nome da categoria: ')
            tipo = input('Tipo da categoria: ')
            wishlist.adicionar_categoria(nome, tipo)
        elif escolha == 2:
             wishlist.listar_categorias()  
        elif escolha == 3:
            nome = input('Nome do item: ')
            preco = float(input('Preço do item: '))
            nome_categoria = input('Nome da categoria: ')
            wishlist.adicionar_item(nome, preco, nome_categoria, status='pendente') 
        elif escolha == 4:
            wishlist.listar_itens()
        elif escolha == 5:
            id_item = int(input('Informe o id do item: '))   
            wishlist.marcar_como_adquirido(id=id_item) 
        elif escolha == 6:
            wishlist.listar_adquiridos()     
        elif escolha == 7:
            break    

if __name__ == '__main__':
    main()
