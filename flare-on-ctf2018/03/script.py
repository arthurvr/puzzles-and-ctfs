import os
import subprocess

from PIL import Image

# https://github.com/lief-project/LIEF
import lief

def get_code(filename):
    binary = lief.parse(filename)
    directory = next(binary.resources.childs)
    subdirectory = next(directory.childs)
    data = bytes(subdirectory.childs[0].content)
    
    code = ''
    for i in range(len(data)):
        if data[i] == 0 and data[i+1] == 0:
            break
        code += chr(data[i]) if data [i] != 0 else ''
            
    return code

def run_exe(filename, code):
    cp = subprocess.Popen([filename], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = cp.communicate(input=bytes(code, encoding="utf-8"))
    return (output[0][47:59].decode('utf-8'), output[0][63:64].decode('utf-8'))

def get_number_from_image(filename):
    img = Image.open(filename).crop([0,0,70,70]).show()
    result = int(input("Number: "))
    return result

flag = " "*50
for exe_file in os.listdir('./FLEGGO'):
    if exe_file.endswith('.exe'):
        code = get_code('./FLEGGO/' + exe_file)
        print('{} => {}'.format(exe_file, code))
        (img_filename, letter) = run_exe('./FLEGGO/' + exe_file, code)
        print('{} => {}'.format(img_filename, letter))
        index = get_number_from_image('./FLEGGO/' + img_filename)
        print('{} => {}'.format(img_filename, index))
        flag  = flag[:index] + letter + flag[index + 1:]
        
    print(flag)
