def print_hi(name):
    print(f'Hi, {name}')


def square(x):
    """Returns square of a number."""
    return x ** 2


if __name__ == '__main__':
    print_hi('PyCharm')
    square_val = 4
    print(f'Returns square of a number {square_val} is {square(square_val)}')
