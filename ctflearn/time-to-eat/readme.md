# Time to Eat

> My friend sent me some Python code, but something tells me he was hungry when he wrote it. Do you think you can put your reverse engineering skills to use and get it to output the flag?

Instead of figuring out what the code does, it seems fast enough to brute force since we get the format of the desired input as a flag. I was going to brute force the middle string too (not just the numbers), but I tried my program with hard coding `eat` first, and that worked :)

See `eat-modified.py` for the code.

One pitfall: First I forgot to format the numbers properly (not adding leading zeroes when necessary). Important, as `009` is in the correct input. Luckily my warning for an input that's too short wasn't deleted by then.

![](https://i.imgur.com/pRKkXko.png)



