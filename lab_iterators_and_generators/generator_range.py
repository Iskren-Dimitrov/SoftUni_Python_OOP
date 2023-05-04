'''Create a generator function called genrange that receives a start (int) and an end (int) upon initialization.\
It should generate all the numbers from the start to the end (inclusive).'''


def genrange(start, end):
    i = start
    n = end
    while i <= n:
        yield i
        i += 1


print(list(genrange(1, 10)))
