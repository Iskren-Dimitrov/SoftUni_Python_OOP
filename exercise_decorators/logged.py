'''Create a decorator called logged. It should return the name of the function that is being called and its parameters.\
It should also return the result of the execution of the function being called. See the examples for more clarification.'''


def logged(func):
    def wrapper(*args):
        return f"you called {func.__name__}({', '.join(str(s) for s in args)})\n" \
               f"it returned {func(*args)}"

    return wrapper


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
