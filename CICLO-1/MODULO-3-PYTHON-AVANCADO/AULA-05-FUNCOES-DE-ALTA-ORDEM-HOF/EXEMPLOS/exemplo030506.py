list_of_inputs = [1, 2, 3, 4, 5]


def function_to_apply(x: int) -> bool:
    return x %2 == 0


# get only even numbers
res = list(filter(function_to_apply, list_of_inputs))
