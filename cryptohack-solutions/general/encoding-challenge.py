from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64
import codecs
import random
import telnetlib
import json

# =================================================
# Communication setup
# =================================================
HOST = "socket.cryptohack.org"
PORT = 13377

tn = telnetlib.Telnet(HOST, PORT)

def readline():
    return tn.read_until(b"\n")


def json_recv():
    line = readline()
    return json.loads(line.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)

    
# =================================================
# Passing all 100 levels
# =================================================
def encode_base64(s):
    return base64.b64decode(s.encode()).decode()
def encode_hex(s):
    return bytearray.fromhex(s).decode()
def encode_rot13(s):
    return codecs.decode(s, 'rot_13')
def encode_bigint(s):
    return bytearray.fromhex(s[2:]).decode()
def encode_utf8(s):
    return "".join([chr(b) for b in s])


for i in range(100):
    received = json_recv()

    if received["type"] == "base64":
        encoded = encode_base64(received["encoded"])
    elif received["type"] == "hex":
        encoded = encode_hex(received["encoded"])
    elif received["type"] == "rot13":
        encoded = encode_rot13(received["encoded"])
    elif received["type"] == "bigint":
        encoded = encode_bigint(received["encoded"])
    elif received["type"] == "utf-8":
        encoded = encode_utf8(received["encoded"])

    to_send = { "decoded": encoded }
    json_send(to_send)
    
received = json_recv()
print("Received flag: ", received["flag"])
