# Local Target

> Smash the stack.

Have a look at the given program. The challenge seems to be to use the `gets`-call for `input` to overwrite the value after it: the `num`.

```c
char input[16];
int num = 64;

printf("Enter a string: ");
fflush(stdout);
gets(input);
```

Because this value is checked after:

```c
if( num == 65 ){
    printf("You win!\n");
    fflush(stdout);
    // Open file
    fptr = fopen("flag.txt", "r");

...
```

The value of `num` starts changing after I input 24 characters. Remember the ASCII table, to get the value 65 we need to input `A`. I always use Python to create my payload:

![](https://i.imgur.com/YiC131I.png)
