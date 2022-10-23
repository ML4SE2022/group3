import struct

def bin2float(b):
    bf = int(b, 2)
    bf = struct.pack('>l', bf)
    return struct.unpack('>f', bf)[0]

print(bin2float('0100000101010100000000000000000'))