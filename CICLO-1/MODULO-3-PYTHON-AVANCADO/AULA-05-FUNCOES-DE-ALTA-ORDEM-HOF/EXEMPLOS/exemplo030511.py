from functools import reduce

list_of_inputs = [1, 2, 3, 4, 5]


def function_to_apply(x: int, y: int) -> int:
    return x * y


res = reduce(function_to_apply, list_of_inputs)

print(res)