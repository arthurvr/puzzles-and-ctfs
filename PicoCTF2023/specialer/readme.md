# Specialer

> Reception of Special has been cool to say the least. That's why we made an exclusive version of Special, called Secure Comprehensive Interface for Affecting Linux Empirically Rad, or just 'Specialer'. With Specialer, we really tried to remove the distractions from using a shell. Yes, we took out spell checker because of everybody's complaining. But we think you will be excited about our new, reduced feature set for keeping you focused on what needs it the most.

I logged in successfully but most commands don't seem to work. One of the only things that works is `echo` it seems. Luckily, bash has some tricks up its sleeve:


```
Specialer$ echo */*
abra/cadabra.txt abra/cadaniel.txt ala/kazam.txt ala/mode.txt sim/city.txt sim/salabim.txt
```

Ah, let's try to read these files. At first I thought this wouldn't work:

```
Specialer$ echo "$(abra/cadabra.txt)"
-bash: ala/kazam.txt: Permission denied
```

But there's another way using the `<` operator:

```
Specialer$ echo "$(<abra/cadabra.txt)"
Nothing up my sleeve!
```

Now, let's hope one of the files contains the flags...

```
Specialer$ echo "$(< ala/kazam.txt)"
return 0 picoCTF{y0u_d0n7_4ppr3c1473_wh47_w3r3_d01ng_h3r3_49193632}
```

