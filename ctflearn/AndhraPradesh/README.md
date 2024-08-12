# AndhraPradesh Assembler Chall 

In this challenge, I have to edit some constants at the start of an assembly file. That should make some tests pass, so that the flag will be printed to the screen. I have to edit `con1` until `con5`.

These lines in the start routine give away what value `con1` should be (namely `0xab`):

```
mov al, [con1]  ; move the value of con1 to the low byte of rax
cmp al, 0xab
je _test2
```

Notice that in `_test2`, a `jne` instruction is used. Anything except `0xcb` will do for `con2`.

```
_test2:
    xor rax, rax
    mov al, [con2]
    cmp al, 0xcb
    jne _test3

    mov r8, 2       ; exit status
    jmp _noflagforyou
```

Have a look at `_test3`: it is clear that `con3` should be made equal to 0x20.

```
_test3:
    mov r8, 3       ; exit status
    xor rax, rax
    mov al, [con3]
    cmp al, 0x20
    ja  _noflagforyou

    mov r8, 4       ; exit status
    xor rax, rax
    mov al, [con3]
    cmp al, 20h
    jb _noflagforyou
```

Have a look at `_test4`:

```
_test4:
    ; https://en.wikibooks.org/wiki/X86_Assembly/X86_Architecture
    mov r8, 5h      ; exit status
    xor rax, rax
    mov al, [con4]
    mov ah, [con5]
    cmp ax, 0baadh
    jne _noflagforyou

    mov r8, 6h      ; exit status
```

This one is a little tricker, but you should realise that the registers `al`, `ah` and `ax` are related. `al` is the lower 8 bits of `ax`, `ah` is the bits 8 through 15 of `ax`. So `con4` should be `0adh` and `con5` should be `0bah`.

In conclusion:

```
con1 db 0xab
con2 db 0x00
con3 db 0x20
con4 db 0adh
con5 db 0bah
```
