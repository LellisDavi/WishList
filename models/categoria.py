class Categoria():
    def __init__(self, nome, tipo):
        self.nome = nome
        if tipo.title() == 'Necessidade' or tipo.title() == 'Desejo':
            self.tipo = tipo
        else:
            raise ValueError('Tipo não permitido')


           
