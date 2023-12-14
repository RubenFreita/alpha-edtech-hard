from functools import reduce

list_of_inputs = [1, 2, 3, 4, 5]


res = reduce(lambda x, y: x * y, list_of_inputs)
print(res)