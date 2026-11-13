import generators


def test_fib():
    assert [x for x in generators.fib(10)] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def test_powers_of():
    powers = generators.powers_of(2)
    assert [next(powers) for _ in range(10)] == [1, 2, 4, 8, 16, 32, 64, 128, 256, 512,]


def test_chain():
    powers = generators.powers_of(10)
    a = (next(powers) for _ in range(5))
    b = generators.fib(4)
    assert list(generators.chain(a, b)) == [1, 10, 100, 1000, 10000, 0, 1, 1, 2, 3]


def test_pairs():
    assert list(generators.pairs(('a','b','c','d','e'))) == [('a', 'b'), ('a', 'c'),
                                                             ('a', 'd'), ('a', 'e'),
                                                             ('b', 'c'), ('b', 'd'),
                                                             ('b', 'e'), ('c', 'd'),
                                                             ('c', 'e'), ('d', 'e')]

def test_flatten():
    a = []
    for f in generators.flatten([[[1, 2], 3], [4, 5]]):
        a.append(f)
    assert a == [1, 2, 3, 4, 5]
