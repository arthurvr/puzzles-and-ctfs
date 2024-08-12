text1 = '''2m{y!"%w2'z{&o2UfX~ws%!._s+{ (&@Vwu{ (&@_w%{v{(&0'''
text2 = '''<Y)8><\9Fbu,Hy4ONC}pxP"4st12wn`?@O$6BgQo7i#gtD|s>3lf=`'''
def ceasar_with_offset(text, n):
    flag = ''
    for i in text:
        charcode = ord(i)+n
        if charcode > 126:
            flag += chr((charcode%127)+32)
        elif charcode < 33:
            flag += chr(charcode+33)
        else:
            flag += chr(charcode)
    if "CTFlearn" in flag:
        print(flag)

for j in range(32, 127):
    ceasar_with_offset(text1, j)
    ceasar_with_offset(text2, j)
