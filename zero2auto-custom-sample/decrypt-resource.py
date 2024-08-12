from arc4 import ARC4

def decrypt(resource_data):
    return ARC4(resource_data[0x0c:0x1b]).decrypt(resource_data[0x1c:])

with open("./resource.bin", mode="rb") as resource_file:
    contents = resource_file.read()
    new_contents = decrypt(contents)
    print(new_contents)
    with open("stage2.exe", mode="wb") as new_resource_file:
        new_resource_file.write(new_contents)
        print("Stage 2 file created.")