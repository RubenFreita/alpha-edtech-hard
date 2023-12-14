from typing import Callable

def create_adder(x: float) -> Callable[[float], float]:
    def adder(y: float) -> float:
        return x + y
    return adder


# função recebe uma função como argumento
# ou retorna uma função
add_1 = create_adder(1)
add_5 = create_adder(5)

print(add_1(10)) # 11
print(add_5(10)) # 15
print(add_5(add_1(10))) # 16

