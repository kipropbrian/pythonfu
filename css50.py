from random import choice
import cowsay


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
