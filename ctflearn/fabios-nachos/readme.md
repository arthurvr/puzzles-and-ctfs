# Fabio's Nachos

> Fabio runs a very popular nacho restaurant. Every week, he takes his last nacho and adds something new to it. Fabio keeps a collection of his favorite nachos on display, but you suspect that the nachos have a deeper meaning.

The challenge text already hints at fibonacci numbers. The given file contains the following:

```
OTI3MzcyNjkyMTkzMDc4OTk5MTc2IDE2NjQxMDI3NzUwNjIwNTYzNjYyMDk2IDgzNjIxMTQzNDg5ODQ4NDIyOTc3IDE1MDA1MjA1MzYyMDY4OTYwODMyNzcgMjI2OTgzNzQwNTIwMDY4NjM5NTY5NzU2ODIgOTI3MzcyNjkyMTkzMDc4OTk5MTc2IDc3Nzg3NDIwNDkgMTM1MzAxODUyMzQ0NzA2NzQ2MDQ5IDQ4MDc1MjY5NzYgNDM1NjY3NzYyNTg4NTQ4NDQ3MzgxMDUgMzI5NTEyODAwOTkgMjE4OTIyOTk1ODM0NTU1MTY5MDI2IDI0Mjc4OTMyMjgzOTk5NzUwODI0NTMgNDgwNzUyNjk3NiA1OTQyNTExNDc1NzUxMjY0MzIxMjg3NTEyNQ=
```

Which is base64 for

```
927372692193078999176 16641027750620563662096 83621143489848422977 1500520536206896083277 22698374052006863956975682 927372692193078999176 7778742049 135301852344706746049 4807526976 43566776258854844738105 32951280099 218922995834555169026 2427893228399975082453 4807526976 59425114757512643212875125
```

These are all fibonacci numbers! Could write a script, but calculating these is tricky and there's not that much anyway... I used an [online table](https://r-knott.surrey.ac.uk/Fibonacci/fibtable.html) instead. The corresponding n for every Fib(n) on the list is:

```
102 -> 927372692193078999176
108 -> 16641027750620563662096
97  -> 83621143489848422977
103 -> 1500520536206896083277
123 -> 22698374052006863956975682
102 -> 927372692193078999176
49  -> 7778742049
98  -> 135301852344706746049
48  -> 4807526976
110 -> 43566776258854844738105
52  -> 32951280099
99  -> 218922995834555169026
104 -> 2427893228399975082453
48  -> 4807526976
125 -> 59425114757512643212875125
```

These first numbers all look within readable ASCII range. Converting those charcode's to a string gives me


```
flag{f1b0n4ch0}
```
