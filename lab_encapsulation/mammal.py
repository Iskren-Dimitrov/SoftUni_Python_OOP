'''Create a class called Mammal. Upon initialization, it should receive a name, a type, and a sound.\
Create a class attribute called kingdom which should not be accessed outside the class and set it to be "animals".\
Create three more instance methods:'''


class Mammal:
    __kingdom = "animals"

    def __init__(self, name: str, type_animal: str, sound: str):
        self.name = name
        self.type = type_animal
        self.sound = sound

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self):
        return Mammal.__kingdom

    def info(self):
        return f"{self.name} is of type {self.type}"


mammal = Mammal("Dog", "Domestic", "Bark")
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())
