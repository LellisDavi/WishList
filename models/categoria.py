class Categoria():
    def __init__(self, nome, tipo, id=None):
        self.nome = nome
        self.id = id
        if tipo.title() == 'Necessidade' or tipo.title() == 'Desejo':
            self.tipo = tipo.title()
        else:
            raise ValueError('Tipo não permitido')


