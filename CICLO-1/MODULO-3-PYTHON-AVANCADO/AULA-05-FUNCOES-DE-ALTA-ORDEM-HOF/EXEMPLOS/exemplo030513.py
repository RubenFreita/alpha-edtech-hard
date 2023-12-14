import time


def print_start(f):
    def new_f(x):
        print("Started...")
        return f(x)

    return new_f

def print_end(f):
    def new_f(x):
        y = f(x)
        print("Ended.")
        return y

    return new_f

@print_start
@print_end
def wait_and_multiply_by_2(x: float) -> float:
    time.sleep(5)
    return 2 * x


x = wait_and_multiply_by_2(3)

print(x)