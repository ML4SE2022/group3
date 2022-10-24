def all_binary_4_tuples():
    for i in range(2**4):
        yield tuple(int(x) for x in bin(i)[2:].zfill(4))

for t in all_binary_4_tuples():
    print(t)