import hashlib

for i in range(11111, 99999):
    candidate = b"ctflag" + str(i).encode("utf-8")
    result = hashlib.md5(candidate)
    if result.hexdigest() == "e82a4b4a0386d5232d52337f36d2ab73":
        print(candidate)
