'''Create a class called sequence_repeat which should receive a sequence and a number upon initialization.\
Implement an iterator to return the given elements, so they form a string with a length - the given number.\
If the number is greater than the number of elements, then the sequence repeats as necessary. For more clarification,\
see the examples:'''

class sequence_repeat:

    def __init__(self, sequence, number: int):
        self.sequence = sequence
        self.number = number
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.number - 1:
            raise StopIteration

        self.index += 1

        return self.sequence[self.index % len(self.sequence)]


result = sequence_repeat('abc', 5)

for item in result:
    print(item, end ='')