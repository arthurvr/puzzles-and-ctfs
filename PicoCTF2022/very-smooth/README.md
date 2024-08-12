# Very Smooth

> Forget safe primes... Here, we like to live life dangerously... >:)

*I think I could've saved myself some work here with [RsaCtfTool](https://github.com/RsaCtfTool/RsaCtfTool).*

The title gives it away: the factors of the given N will be [smooth](https://en.wikipedia.org/wiki/Smooth_number). There exists a special-purpose algorithm for finding such factors easily: [Pollard's `p-1` algorithm](https://en.wikipedia.org/wiki/Pollard%27s_p_%E2%88%92_1_algorithm).
I implemented this algorithm in python in `solution.py`. Using some utility
functions and number theory libraries this can be done in a few lines. The value for `e` was in
`gen.py`, the `n` value and the ciphertext were in `output.txt`. 

![](https://i.imgur.com/9xjpKlp.png)

