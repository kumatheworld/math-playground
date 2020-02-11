from itertools import chain, combinations

def powerset(g):
    """Powerset"""
    s = list(g)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def R(alpha):
    """Well founded set that constitutes HF"""
    if alpha == 0:
        return iter(())
    else:
        return powerset(R(alpha-1))

def hotbits(m):
    """Places in which there's 1 in binary representation of input"""
    i = 0
    while m:
        if m & 1:
            yield i
        i += 1
        m >>= 1

def omega2hf(m):
    """Natural bijection from N to HF"""
    if m == 0:
        return iter(())
    else:
        for n in hotbits(m):
            yield omega2hf(n)

def tuplify_nested_generator(g):
    """Recursive tuplification"""
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
