from typing import Union, Tuple
from math import sqrt
from cmath import sqrt as raiz_complexa

def delta(a: float, b: float , c: float) -> Union[int, float]:
    return b**2 - 4*a*c


def bhaskara(a: float, b: float, c: float) -> Tuple[Union[complex, float], Union[complex, float]]:
    d = delta(a,b,c)

    if d >= 0:
        x1 = (-b + sqrt(d))/2*a
        x2 = (-b - sqrt(d))/2*a
        return x1, x2
    else:
        y1 = (-b + raiz_complexa(d))/2*a
        y2 = (-b - raiz_complexa(d))/2*a
        return y1, y2

#instância raízes com números complexos
a = 3
b = 2
c = 4
print()
print(f"As raízes da equação {a}*x^2 + {b}*x + {c} = 0 são:")
print(bhaskara(a,b,c))

#instância normal
a = 2
b = 5
c = 2
print()
print(f"As raízes da equação {a}*x^2 + {b}*x + {c} = 0 são:")
print(bhaskara(a,b,c))
