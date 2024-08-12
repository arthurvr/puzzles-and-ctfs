# Picker III

> Can you figure out how this program works to get the flag?

Using the program, you can read and write variables. However, you can also overwrite variables that exist! You can write over `func_table` to make it possible to call the `win()` function.

However, there is a check in place: the length of the `func_table` variable should stay equal to `FUNC_TABLE_SIZE * FUNC_TABLE_ENTRY_SIZE`, which is 128. You can create a `func_table` this long by simply adding the right amount of padding.

![](https://i.imgur.com/4dqfr1L.png)

Again, the flag is given in hexadecimal ASCII characters: I used CyberChef to decode these.
