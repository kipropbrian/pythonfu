# https://dbader.org/blog/python-iterators


class BoundedRepeater:
    def __init__(self, value, max_repeats) -> None:
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >=self.max_repeats:
            raise StopIteration

        self.count += 1
        return self.value

repeater = BoundedRepeater('Hello', 4)
for item in repeater:
    print(item)


class Repeater:
    def __init__(self, value) -> None:
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value

repeater = Repeater('Hello')

for item in repeater:
    print(item)


# range usage

for i in reversed(range(5)):
    print(i)
