# ropfu

> What's ROP?

Return-oriented programming is an exploit technique for buffer overflow vulnerabilities.

* The vulnerability itself is clear: again an uncontrolled `gets` statement. There's no function now that prints the flag -- instead we're asked to spawn a usable shell.

* We can use gdb and peda patterns again to figure out our overflow offset. This time the return address is at offset 28.

* Let's use a tool called *ROPGadget* now to build our ROP chain. The command we use is:

```
ROPgadget --binary ./vuln --ropchain  --badbytes "00|Oa"
```

(We indicate not to use bytes `00` or `0a`: newlines or null bytes.)

* I modified the program it gives me to use pwntools instead. Pwntools makes a reverse shell a lot easier to work with. I also added a debug flag to either work on the local program or the remote one.

* See `exploit.py` for the final program. Works both locally and on the remote machine!
