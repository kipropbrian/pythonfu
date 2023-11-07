class Student:
    def __init__(self, name, house, patronus=None) -> None:
        if not name:
            raise ValueError("Invalid name")

        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self) -> str:
        return f"{self.name} is of house {self.house} and charm {self.charm()}"

    def charm(self) -> str:
        match self.patronus:
            case "Stag":
                return "🤪"
            case "Otter":
                return "👁️"
            case _:
                return "👻"

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Grif", "Rav", "Traps"]:
            raise ValueError("Invalid house")
        self._house = house

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    student = get_students()
    print(student)


def get_students():
    student = Student.get()
    patronus = input("Patronus: ")
    return Student(student.name, student.house, patronus)


if __name__ == "__main__":
    main()
