'''Strange Numbers'''


# isStrange :: Int -> Bool
def isStrange(n):
    '''True if all consecutive decimal digit
       pairs in n have a prime difference.
    '''
    def test(a, b):
        return abs(a - b) in [2, 3, 5, 7]

    xs = digits(n)
    return all(map(test, xs, xs[1:]))


# ------------------- TEST AND DISPLAY -------------------
# main :: IO ()
def main():
    '''List and count of Strange numbers'''

    xs = [
        n for n in range(100, 1 + 500)
        if isStrange(n)
    ]
    print('\nStrange numbers in range [100..500]\n')
    print('(Total: ' + str(len(xs)) + ')\n')
    print(
        '\n'.join(
            ' '.join(
                str(x) for x in row
            ) for row in chunksOf(10)(xs)
        )
    )


# ----------------------- GENERIC ------------------------

# chunksOf :: Int -> [a] -> [[a]]
def chunksOf(n):
    '''A series of lists of length n, subdividing the
       contents of xs. Where the length of xs is not evenly
       divible, the final list will be shorter than n.
    '''
    def go(xs):
        return (
            xs[i:n + i] for i in range(0, len(xs), n)
        ) if 0 < n else None
    return go


# digits :: Int -> [Int]
def digits(n):
    '''Component digits of a decimal number.'''
    return [int(c) for c in str(n)]


# MAIN ---
if __name__ == '__main__':
    main()