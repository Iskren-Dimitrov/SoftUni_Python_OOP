'''Create a generator function called possible_permutations() which should receive\
a list and return lists with all possible permutations between its elements.'''

from itertools import permutations


def possible_permutations(sequence):
    for el in list(permutations(sequence)):
        yield list(el)


[print(n) for n in possible_permutations([1, 2, 3])]
