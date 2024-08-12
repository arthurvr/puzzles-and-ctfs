import socket
import uuid
import sys

name = "Arthur"

def getHexName():
    return ''.join(["{:02x}".format(ord(x)) for x in name])

def getMAC():
    return ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1])

def getHostname():
    return socket.gethostname()

def getIpAddy():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("arthurverschaeve.be", 80))
    return s.getsockname()[0]

def getFinalResultFromHexName():
    a = int(getHexName()) & 0xFFFFFFFF
    b = int(getMAC()[3]) 
    s1 = (a + 171) & 0xFFFFFFFF
    s2 = (a + 15658734) & 0xFFFFFFFF
    s3 = (s1 ^ b) + ((b + s2) ^ 0x33838D) & 0xFFFFFFFF
    s4 = 978670 * b & 0xFFFFFFFF
    return s3 + s4 + a & 0xFFFFFFFF

serial = str(getMAC()[3]) + str(getIpAddy()[1]) + str(getFinalResultFromHexName()) + str(getHostname()[0])
print(serial)