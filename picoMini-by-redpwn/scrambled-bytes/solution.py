from scapy.all import *
import random

# Read capture file and filter the correct packets
conf.layers.filter([Ether, IP, UDP])
capture = rdpcap('capture.pcapng')
packets = capture.filter(lambda p: UDP in p and p[UDP].dport == 56742)
data = bytearray(b''.join(p[UDP][Raw].load for p in packets))

# Use the same seed as before
# Notice that this is the exact timestamp (even though wireshark seems to show a relative one)
random.seed(int(packets[0].time))

# Trick to "unshuffle" the random order: first decide the shuffle order
order = [*range(len(data))]
random.shuffle(order)

# "Decrypt"
for i in range(len(data)):
    random.randrange(65536) # don't forget this call to randrange!
    data[i] ^= random.randrange(256)

# ... and now actually unshuffle
result = bytearray(len(data))
for i, x in enumerate(order):
    result[x] = data[i]

# Write the resulting bytes to a file
with open("output", "wb") as f:
    f.write(result)
