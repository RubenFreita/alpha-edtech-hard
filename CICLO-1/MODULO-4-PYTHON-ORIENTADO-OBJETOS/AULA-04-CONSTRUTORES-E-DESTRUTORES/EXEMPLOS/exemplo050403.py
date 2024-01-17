import math


class Point:
    """ Point classe para representar e manipular coordinadas X, Y. """
    def __init__(self, initX=0, initY=0):
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y


class Turtle:
    idTurtle: int = 0
    id: int
    nameTurtle: str
    position: Point
    direction: float

    # Implementar método construtor
    def __init__(self, position=Point(0, 0), direction=90, nameTurtle="Tx"):
        # Atribuir o ID sequencial ao objeto e, em seguida, incrementar para o próximo objeto
        self.id = Turtle.idTurtle
        Turtle.idTurtle += 1
        # atributos iniciais
        self.position = position
        self.direction = direction
        self.nameTurtle = nameTurtle

    def getPosition(self) -> Point:
        return self.position

    def andar(self, steps=1) -> None:
        self.position = Point( self.position.getX() + steps * math.sin(self.direction),
                               self.position.getY() + steps * math.cos(self.direction) )

    def girar(self, angle=-90) -> None:
        self.direction += angle
        if self.direction < 0:
            self.direction += 360
        if self.direction > 360:
            self.direction -= 360

    # Implementar método imprimir
    # def __str__(self) -> str:
    #     return f"{self.nameTurtle} id={self.id} position -> (x={self.position.getX()}; y={self.position.getY()}) direction={self.direction}"


# origem = Point(0, 0)
# print(origem.getX())
# print(origem.getY())

rafael = Turtle(Point(0, 0), 0, "Rafael")
print("rafael.id=", rafael.id)
donatello = Turtle(Point(0, 200), 0, "Donatello")
print("donatello id=", donatello.id)
michelangelo = Turtle(position=Point(initX=100, initY=200),
                      direction=180, nameTurtle="Miguel")
print("michelangelo id=", michelangelo.id)
leonardo = Turtle(position=Point(initY=0, initX=100),
                  nameTurtle="Leonardo",
                  direction=270)
print("leonardo id=", leonardo.id)

#print(rafael)
#print(donatello)
#print(michelangelo)
#print(leonardo)

import random

megan = Turtle(Point(random.uniform(0, 600), random.uniform(0, 800)), 0, "Megan Fox")
print(megan.id)

#listPontos = [rafael.position, donatello.position, michelangelo.position,
#              leonardo.position, megan.position]
