def print_hi(name):
    print(f'Hi, {name}')


def square(x):
    """Returns square of a number."""
    return x ** 2


def primeNumber(num):
    for n in range(2, num):
        for i in range(2, int(n ** 0.5) + 1):
            if n%i ==0:
                break
            else:
             print(f'val = {i}')


if __name__ == '__main__':
    print_hi('PyCharm')
    square_val = 4
    print(f'Returns square of a number {square_val} is {square(square_val)}')
    primeNumber(11)
