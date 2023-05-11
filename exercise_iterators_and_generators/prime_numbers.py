'''Create a generator function called get_primes() which should receive a list of integer numbers\
and return a list containing only the prime numbers from the initial list.\
You can learn more about prime numbers from here:'''

import math
from typing import List


def get_primes(numbers: List[int]):
    for number in numbers:
        if number <= 1:
            continue

        for num in range(2, int(math.sqrt(number)) + 1):
            if number % num == 0:
                break
        else:
            yield number


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
