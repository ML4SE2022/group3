from itertools import chain, cycle, accumulate, combinations
from typing import List, Tuple

# %% Factors

def factors5(n: int) -> List[int]:
    """Factors of n, (but not n)."""
    def prime_powers(n):
        # c goes through 2, 3, 5, then the infinite (6n+1, 6n+5) series
        for c in accumulate(chain([2, 1, 2], cycle([2,4]))):
            if c*c > n: break
            if n%c: continue
            d,p = (), c
            while not n%c:
                n,p,d = n//c, p*c, d + (p,)
            yield(d)
        if n > 1: yield((n,))

    r = [1]
    for e in prime_powers(n):
        r += [a*b for a in r for b in e]
    return r[:-1]

# %% Powerset

def powerset(s: List[int]) -> List[Tuple[int, ...]]:
    """powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3) ."""
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))

# %% Practical number

def is_practical(x: int) -> bool:
    """
    Is x a practical number.

    I.e. Can some selection of the proper divisors of x, (other than x), sum
    to i for all i in the range 1..x-1 inclusive.
    """
    if x == 1:
        return True
    if x %2:
        return False  # No Odd number more than 1
    f = factors5(x)
    ps = powerset(f)
    found = {y for y in {sum(i) for i in ps}
             if 1 <= y < x}
    return len(found) == x - 1


if __name__ == '__main__':
    n = 333
    p = [x for x in range(1, n + 1) if is_practical(x)]
    print(f"There are {len(p)} Practical numbers from 1 to {n}:")
    print(' ', str(p[:10])[1:-1], '...', str(p[-10:])[1:-1])
    x = 666
    print(f"\nSTRETCH GOAL: {x} is {'not ' if not is_practical(x) else ''}Practical.")