class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return f"{self.name} {other.surname}"


class Group:
    def __init__(self, name, people: list):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        new_instance_name = f"{self.name} {other.name}"
        new_instance_people = self.people + other.people
        return Group(new_instance_name, new_instance_people)

    def __repr__(self):
        return f"Group {self.name} with members {', '.join(str(person) for person in self.people)}"

    def __getitem__(self, item):
        return f"Person {item}: {self.people[item]}"
