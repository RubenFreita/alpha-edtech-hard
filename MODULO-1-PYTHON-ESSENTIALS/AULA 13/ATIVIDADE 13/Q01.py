

# def fatorial(n):
#     fat = 1
#     for i in range(1, n+1):
#         fat *= i
#     return fat

def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n-1)

print(f"Fatorial de 0: {fatorial(0)}")
print(f"Fatorial de 1: {fatorial(1)}")
print(f"Fatorial de 2: {fatorial(2)}")
print(f"Fatorial de 3: {fatorial(3)}")
print(f"Fatorial de 4: {fatorial(4)}")
print(f"Fatorial de 5: {fatorial(5)}")
