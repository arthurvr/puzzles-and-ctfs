# Collider

Looking at the given Python file, it looks like the flag will leak when we input an MD5 collision. That means we need two different inputs, with the same hash. Luckily, for MD5, several of these collisions are known. I used the one from [this paper](https://eprint.iacr.org/2010/643).

![](https://i.imgur.com/C0svTyX.png)
