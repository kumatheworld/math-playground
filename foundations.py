from itertools import chain, combinations

def powerset(g):
    """Returns the powerset of g"""
    s = list(g)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def R(n):
    """Returns the set of well-founded sets of rank < n"""
    if n == 0:
        return iter(())
    else:
        return powerset(R(n-1))

def hotbits(m):
    """Returns the places in which there's 1 in the binary representation of m"""
    i = 0
    while m:
        if m & 1:
            yield i
        i += 1
        m >>= 1

def omega2hf(m):
    """Returns the image of m by the natural bijection from N to HF"""
    if m == 0:
        return iter(())
    else:
        for n in hotbits(m):
            yield omega2hf(n)

def tuplify_nested_generator(g):
    """Tuplify g Recursively"""
    return tuple(
        tuplify_nested_generator(gg)
        for gg in g
    )

def test():
    print(tuple(powerset(range(3))))
    print(tuple(R(4)))
    print(tuple(hotbits(43)))
    print(tuplify_nested_generator(omega2hf(123456789123456789)))

if __name__ == '__main__':
    test()
