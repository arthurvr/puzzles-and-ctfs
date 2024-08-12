# X AND OR

Using Ghidra, the given file's `main` function looks remarkebly easy:

```c
undefined8 main(void)

{
  int iVar1;
  size_t sVar2;
  long in_FS_OFFSET;
  char local_118 [264];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  printf("Enter the flag: ");
  fgets(local_118,0x100,stdin);
  sVar2 = strcspn(local_118,"\r\n");
  local_118[sVar2] = '\0';
  sVar2 = strnlen(local_118,0x100);
  iVar1 = (*code)(local_118,sVar2 & 0xffffffff);
  if (iVar1 == 0) {
    puts("That is the flag!!!!");
  }
  else {
    puts("That is not the flag.");
  }
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}

```

However, `code` doesn't look like a function as it's represnted in this decompilation view. It's an area in memory instead. By checking the references there, I found out `init` does more than it usually does:

```c  
int init(EVP_PKEY_CTX *ctx)

{
  long lVar1;
  
  code = (undefined *)mmap((void *)0x0,0x1000,7,0x22,0,0);
  *code = 0x55;
  lVar1 = 1;
  do {
    code[lVar1] = (&check_password)[lVar1] ^ 0x42;
    lVar1 = lVar1 + 1;
  } while (lVar1 != 500);
  return 500;
}
```

`code` only becomes executable at runtime... and it contains whatever is in `check_password` XOR `0x42`.

I used the built-in Ghidra script `XorMemoryScript` to XOR the bytes inside of `check_password`, and then disassembled the result. The result is the following:

```c
undefined8 UndefinedFunction_00102048(undefined8 param_1,undefined4 param_2)

{
  undefined8 uVar1;
  long unaff_RBP;
  long in_FS_OFFSET;
  
  *(undefined8 *)(unaff_RBP + -0x48) = param_1;
  *(undefined4 *)(unaff_RBP + -0x4c) = param_2;
  *(undefined8 *)(unaff_RBP + -8) = *(undefined8 *)(in_FS_OFFSET + 0x28);
  *(undefined8 *)(unaff_RBP + -0x30) = 0x3136483b7c696d66;
  *(undefined8 *)(unaff_RBP + -0x28) = 0x786c31631977283e;
  *(undefined8 *)(unaff_RBP + -0x20) = 0x4e267d3d63334e24;
  *(undefined8 *)(unaff_RBP + -0x18) = 0x31311c232b303937;
  *(undefined4 *)(unaff_RBP + -0x10) = 0x1b74296a;
  *(undefined2 *)(unaff_RBP + -0xc) = 0x7c62;
  *(undefined *)(unaff_RBP + -10) = 0;
  *(undefined4 *)(unaff_RBP + -0x34) = 0x26;
  if (*(int *)(unaff_RBP + -0x34) == *(int *)(unaff_RBP + -0x4c)) {
    *(undefined4 *)(unaff_RBP + -0x38) = 0;
    while (*(int *)(unaff_RBP + -0x38) < *(int *)(unaff_RBP + -0x34)) {
      if (((int)*(char *)(unaff_RBP + -0x30 + (long)*(int *)(unaff_RBP + -0x38)) ^
          (*(int *)(unaff_RBP + -0x38) % 6) * (*(int *)(unaff_RBP + -0x38) % 6) *
          (*(int *)(unaff_RBP + -0x38) % 6)) !=
          (int)*(char *)(*(long *)(unaff_RBP + -0x48) + (long)*(int *)(unaff_RBP + -0x38))) {
        return 0xffffffff;
      }
      *(int *)(unaff_RBP + -0x38) = *(int *)(unaff_RBP + -0x38) + 1;
    }
    uVar1 = 0;
  }
  else {
    uVar1 = 0xffffffff;
  }
  return uVar1;
}
```

This does the following:

* We know the two parameters are the flag and its length.
* First, the following bytes are stored: `7c621b74296a31311c232b3039374e267d3d63334e24786c31631977283e3136483b7c696d66` (think about the order!). Call this `A`.
* The first if-statement checks if the length is equal to `0x26`.
* Inside, there's a `while` loop with `*(int *)(unaff_RBP + -0x38)` a counter always increasing by one. Call this counter `i`.
* Every character of the given flag is checked against `A[i] ^ (i%6) * (i%6) * (i%6)`.
* `0` is returned if all characters match, `0xffffffff` if not.

We're looking for such a zero return value (see `main`), so we can do that calculation ourselves to find out the right flag. The following Python script does that:

```python
A = bytearray.fromhex("7c621b74296a31311c232b3039374e267d3d63334e24786c31631977283e3136483b7c696d66")

flag = ""

for i in range(0x26):
    char = A[- (i + 1)] ^ (i % 6) * (i % 6) * (i % 6)
    flag += chr(char)

print(flag)
```

(Notice we're using A in reverse order here: little-endian!)

The script prints the following, which is the right flag:

```
flag{560637dc0dcd33b5ff37880ca10b24fb}
```

