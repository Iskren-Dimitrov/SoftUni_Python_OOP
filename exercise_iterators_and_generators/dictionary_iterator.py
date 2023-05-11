'''Create a class called dictionary_iter. Upon initialization, it should receive a dictionary object.\
Implement the iterator to return each key-value pair of the dictionary\
as a tuple of two elements (the key and the value).'''


class dictionary_iter:

    def __init__(self, dictionary: dict):
        self.items = list(dictionary.items())  # ((1, '1'), (2, '2'))
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items) - 1:
            raise StopIteration

        self.index += 1

        return self.items[self.index]


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
