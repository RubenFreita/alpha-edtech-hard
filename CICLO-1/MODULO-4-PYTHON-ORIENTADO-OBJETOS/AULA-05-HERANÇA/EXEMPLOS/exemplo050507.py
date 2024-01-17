class Pai(object):
    def __init__(self):
        print('Construindo a classe Pai')


class Mae(object):
    def __init__(self):
        print('Construindo a classe Mae')


class Filha(Mae):
    def __init__(self):
        Pai.__init__(self)
