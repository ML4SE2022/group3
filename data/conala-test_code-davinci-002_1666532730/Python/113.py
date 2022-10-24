def hex_to_float(h):
    return struct.unpack('>f', h.decode('hex'))[0]