list_of_inputs = [1, 2, 3, 4, 5]

res = [x ** (1 / 2) for x in list_of_inputs if x % 2 == 0]

print(res)