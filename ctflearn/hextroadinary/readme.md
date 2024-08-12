# Hextroadinary

> Meet ROXy, a coder obsessed with being exclusively the worlds best hacker. She specializes in short cryptic hard to decipher secret codes. The below hex values for example, she did something with them to generate a secret code, can you figure out what? Your answer should start with 0x.

> 0xc4115 0x4cf8

There's a hint in the name: just XOR the two values.

```python
>>> format(0xc4115 ^ 0x4cf8, '#x')
'0xc0ded'
```



