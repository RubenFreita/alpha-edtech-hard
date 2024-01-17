class English(object):
    def greet(self):  
        print("Hi!")


class Portuguese(object):
    def greet(self):
        print("Oi!")


class Bilingual(English, Portuguese):
    pass


if __name__ == '__main__':
    Bilingual().greet()
