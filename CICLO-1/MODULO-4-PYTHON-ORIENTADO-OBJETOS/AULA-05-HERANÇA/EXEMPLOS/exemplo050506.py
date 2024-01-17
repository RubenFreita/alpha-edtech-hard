class Pai(object):
    def __init__(self):
        print('Construindo a classe Pai')


class Filha(Pai):
    def __init__(self):
        Pai.__init__(self)
