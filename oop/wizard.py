class Wizard:
    def __init__(self, name) -> None:
        self.name = name

class Student(Wizard):
    def __init__(self, name, subject) -> None:
        super().__init__(name)
        self.subject = subject
    
    ...

class Professor(Wizard):
    ...