""" Exercises to practice building generators"""
from collections.abc import Sequence, Generator
from typing import Any

# Up til now, we have always written functions that perform some computation
# and returned a value or tuple of values. This works in many situations, but
# what if we have some large, maybe infinite, computation to complete, but we
# also only require parts of it at a time? That's where **generators** come in.

# Generators are like functions, but instead of **return**ing a value or tuple of
# values, they **yield** values one at a time. We're going to start playing with
# generators by rewriting our Fibonacci function to produce a stream of Fibonacci
# numbers instead of finding the n-th one.

def fib(stop: int|None = None) -> Generator[int]:
    """Generate a stream of Fibonacci numbers. """
    f2 = 0
    yield f2
    f1 = 1
    yield f1
    n = 1
    while stop is None or n < stop:
        f = f2 + f1
        yield f
        f2, f1 = f1, f
        n += 1


def powers_of(n: int) -> Generator[int]:
    """Generate a stream of powers of n"""
    count = 0
    while True:
        yield n**count
        count += 1

        
def chain(*sequences: Sequence[Any]) -> Generator[Sequence]:
    """Generate a single sequence from sequences"""
    for sequence in sequences:
        for item in sequence:
            yield item

    
def pairs(items: Sequence[Any]) -> Generator[tuple[Any, Any]]:
    """Generate each unique pair of items. Raises a ValueError if provided with less than two items."""
    if len(items) < 2:
        raise ValueError
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            yield items[i], items[j]


def flatten(nested: Sequence[Any]) -> Generator[Any]:
    """Generate a stream of items from the nested sequence in the order they appear"""
    # Hint: each time you come across a Sequence, `yield from flatten(subsequence)`
    for item in nested:
        if isinstance(item, Sequence) and not isinstance(item, str):
            yield from flatten(item)
        else:
            yield item

if __name__ == "__main__":
    for f in fib(10):
        print(f)
        # should produce 0 1 1 2 3 5 8 13 21 34 55

    power_count = 0
    power_stop = 10
    for power in powers_of(2):
        power_count += 1
        print(power)
        if power_count >= power_stop:
            break
        # should produce 1 2 4 8 16 32 64 128 256 512 1024

    for c in chain([0, 1, 2], [5, 6, 7], ["a", "b", "c", "d"], []):
        print(c)
        # should produce 0, 1, 2, 5, 6, 7, "a", "b", "c", "d',

    for p in pairs(range(8)):
        print(p)
        # should print (0,1) (0,2) (0,3) ... (6,7)

    for f in flatten([1, 2, [3, 4, 5], "hello", 6, 7, ["a", "b", "c"]]):
        print(f)
        # should print 1 2 3 4 5 hello 6 7 a b c