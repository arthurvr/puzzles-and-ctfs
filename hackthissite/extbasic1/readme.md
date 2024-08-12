# Extended basics 1

The following program is given, and we're asked for an input string that will crash the program:

```c
void blah(char *str)
 {
         char lol[200];
         strcpy(lol, str);
 }
 
```

Any string longer than 200 characters won't fit in the buffer and makes the program crash.