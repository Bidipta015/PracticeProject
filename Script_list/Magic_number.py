"""A magic square is an arrangement of numbers in a square, where the sum of the numbers in each row, each column,
and each diagonal will be equal to the same number. For example, if the number of rows and columns in a magic square is "n", then it will have
n×n numbers.

You can create a magic square of any number "n" except when 𝑛=2
n=2. The constant which is the sum of every row, column, and diagonal is called the magic constant, M. Every magic square will have this constant 𝑀,
which is based on the value of 𝑛. The smallest 'nontrivial' case, which is a 3×3
square, has a magic constant of 15.
"""


def generator_Magic(n1):
    for number in range(3, n1 + 1):
        magic_number = (number * (number ** 2 + 1)) // 2
        yield magic_number  # Yield the magic constant which is an iterator to store as list and iterate the list in
        # sequence


if __name__ == '__main__':
    n = int(input("Enter the value of n1: ").strip())  # Input for n1

    for i in generator_Magic(n):
        print(int(i))  # Print each magic constant as an integer

    gen1 = generator_Magic(n)
    print(type(gen1))
