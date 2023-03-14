'''Follow the diagram and create all the classes. Except for the Animal class, each class should inherit from another\
class, as shown in the diagram. The Animal class should receive a name - string upon initialization.
Every class should have a constructor, which accepts one parameter: name

Example:

from project.lizard import Lizard
from project.mammal import Mammal

mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)'''
