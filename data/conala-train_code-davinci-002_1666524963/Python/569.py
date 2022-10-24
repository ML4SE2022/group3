import socket
import struct

def ip2long(ip):
    """
    Convert an IP string to long
    """
    packedIP = socket.inet_aton(ip)
    return struct.unpack("!L", packedIP)[0]

def long2ip(ip):
    """
    Convert a long to IP
    """
    return socket.inet_ntoa(struct.pack('!L', ip))

print ip2long('192.168.1.1')
print long2ip(3232235777)