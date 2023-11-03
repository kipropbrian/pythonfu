from random import choice
import pytest


def name():
    name = input("whats your name ")
    print(f" Your name is {name} !")


def is_even(n):
    return n % 2 == 0


def print_box(n):
    for _ in range(n):
        for _ in range(n):
            print("#", end="")
        print()


def print_triangle(n):
    start = 0
    while start <= n:
        start += 1
        print("*" * start)


def try_excepts():
    try:
        x = int(input("What's x? "))
        print(f"x is {x}")
    except ValueError:
        # pass is silent
        print("x is not an integer")


from random import choice


def try_random():
    heads = tails = total = 0
    heads_percentage = tails_percentage = (0.0,)
    try:
        while True:
            coin = flip_endless()
            total += 1
            if coin == "heads":
                heads += 1
            else:
                tails += 1

            heads_percentage = (heads / total) * 100
            tails_percentage = (tails / total) * 100

            print(
                f"Heads => {heads_percentage:.2f}% \nTails => {tails_percentage:.2f}% \nTotal => {total}"
            )
    except KeyboardInterrupt:
        # If you stop the function with a keyboard interrupt, it will print the final counts
        print(f"\nFinal counts:")
        print(
            f"Heads => {heads_percentage:.2f}% \nTails => {tails_percentage:.2f}% \nTotal => {total}"
        )


def flip_endless() -> str:
    return choice(["heads", "tails"])


## Testing


def main_():
    x = int(input("What's x? "))
    print("x squared is ", square(x))


def square(n):
    return n * n


def test_square_old():
    if square(2) != 4:
        print("Error: 2 squared was not 4")
    if square(3) != 9:
        print("Error: Square of 3 was not 9")


def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("Error: 2 squared was not 4")

    try:
        assert square(3) == 9
    except AssertionError:
        print("Error: 2 squared was not 4")


# using pytest
def test_pytestsquare():
    assert square(2) == 4
    assert square(3) == 9


def test_zero():
    assert square(0) == 0


def test_negative():
    assert square(-4) == 16


def test_str():
    with pytest.raises(TypeError):
        square("Cat")


def inputsio():
    with open("names.txt", "a") as file:
        name = input("What's your name? ")
        file.write(f"{name}\n")

    with open("names.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        print("Hello,", line.rstrip())


def inputsorted():
    names = []
    with open('names.txt') as file:
        for line in sorted(file):
            print(line.rstrip())
        
