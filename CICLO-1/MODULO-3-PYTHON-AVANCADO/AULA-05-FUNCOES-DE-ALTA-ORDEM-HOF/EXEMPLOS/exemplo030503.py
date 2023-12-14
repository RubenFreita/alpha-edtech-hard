list_of_inputs = [1, 2, 3, 4, 5]


def function_to_apply(x: int) -> float:
    return x ** (1/2)


res = list(map(function_to_apply, list_of_inputs))
