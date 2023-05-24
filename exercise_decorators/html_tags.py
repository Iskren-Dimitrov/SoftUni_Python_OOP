'''Create a decorator called tags. It should receive an HTML tag as a parameter,\
wrap the result of a function with the given tag and return the new result. For more clarification,\
see the examples below'''


def tags(html_tag):
    def some_func(func):
        def wrapper(*args):
            return f"<{html_tag}>{func(*args)}</{html_tag}>"

        return wrapper

    return some_func


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))
