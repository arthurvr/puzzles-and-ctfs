# Lazy Game Challenge

> I found an interesting game made by some guy named "John_123". It is some betting game. I made some small fixes to the game; see if you can still pwn this and steal $1000000 from me!

After playing the game it's obvious that we can't really win the money. No broken PRNG or anything like that. However, there's another trick we can use: a logical vulnerability. If you bet `-1000000`, and lose, your new balance becomes `500 - (-1000000)` :-)
