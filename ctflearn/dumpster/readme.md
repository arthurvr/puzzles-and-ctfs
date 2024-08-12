# Dumpster

> I found a flag, but it was encrypted! Our systems have detected that someone has successfully decrypted this flag, and we stealthily took a heap dump of the program (in Java). Can you recover the flag for me? Here's the source code of the Java program and the heap dump.

This was a challenging one for me. I know some Java programming, but I have no Java forensics or reverse engineering experience. After some searching around, I found the [VisualMVM](https://visualvm.github.io/gettingstarted.html) program to inspect the given `.hprof` file.

It seemed useful to look at the information inside `Decryptor.main` first, and indeed, the passHash variable was in there:

![](https://i.imgur.com/x8RJDMV.png)

This was the most important step. Now I just had to write a Java program that imitates `Decryptor.java` to find the flag with a given hash. I did so in `solution.py` and it worked:

![](https://i.imgur.com/zLNXOih.png)
