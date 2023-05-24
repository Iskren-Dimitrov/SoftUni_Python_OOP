'''Create a decorator called type_check. It should receive a type (int/float/str/…),\
and it should check if the parameter passed to the decorated function is of the type given to the decorator.\
If it is, execute the function and return the result, otherwise return "Bad Type".'''


def type_check(num):
    def some(func):
        def wrapper(*args):
            for arg in args:
                if isinstance(arg, num):
                    return func(*args)
                return "Bad Type"

        return wrapper

    return some


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
