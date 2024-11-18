def demonstrate_len():
    print("Using len:")
    print(f"len('hello') -> {len('hello')}")
    print(f"len([1, 2, 3, 4, 5]) -> {len([1, 2, 3, 4, 5])}")
    print()


def demonstrate_type():
    print("Using type:")
    print(f"type('hello') -> {type('hello')}")
    print(f"type([2, 3]) -> {type([2, 3])}")
    print(f"type(123) -> {type(123)}")
    print()


def demonstrate_range():
    print("Using range:")
    print(f"list(range(10, 13)) -> {list(range(10, 13))}")
    print(f"list(range(3)) -> {list(range(3))}")
    print()


def iteration_process():
    x = [6, 4, 6, 7, 8, 2]
    '''Using Iterate function to navigate iterated objects in python'''
    iteration = iter(x)
    print(f'Iteration 1 {next(iteration)}')
    print(f'Iteration 2 {next(iteration)}')
    print(f'Iteration 3 {next(iteration)}')
    print(f'Iteration 4 {next(iteration)}')
    print(f'Iteration 5 {next(iteration)}')
    print(f'Iteration 6 {next(iteration)}')
    '''optimised way - Iteration of list'''
    for position, value in enumerate(x):  # Use enumerate for position tracking
        print(f"Iteration loop position {position} : {value}")
    '''Alternative process'''
    print("Iterating through the list with positions:")
    while True:
        try:
            print(next(iteration))
        except StopIteration:
            break


def main():
    print("Demonstrating len, type, and range:")
    print("-----------------------------")
    demonstrate_len()
    demonstrate_type()
    demonstrate_range()
    iteration_process()


if __name__ == "__main__":
    main()
