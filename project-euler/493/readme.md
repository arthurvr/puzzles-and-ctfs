## [Project Euler - Problem 493](https://projecteuler.net/problem=493)

> 70 coloured balls are placed in an urn, 10 for each of the seven rainbow colours.

> What is the expected number of distinct colours in 20 randomly picked balls?

> Give your answer with nine digits after the decimal point (`a.bcdefghij`).

Like often in probability-calculations, thinking about the inverse of (part of) the problem is easier: What is the probability that this color is not among the 20 picked balls? We can calculate that as the probability that 20 out of 70 balls are actually taken from the set of only 60 balls with a different colour. That's `(60 choose 20) / (70 choose 20)`.

Invert this, and we get the propability that a color was picked: `1 - (60 choose 20) / (70 choose 20)`.

For seven colours, that's `7 * [1 - (60 choose 20) / (70 choose 20)]`.

Implementing this binomial coefficent requires an efficient algorithm, which is sure interesting [to implement](https://en.wikipedia.org/wiki/Binomial_coefficient). I had done that a few times before, and besides that, this is an exact formula so inputting this in a calculator didn't feel like cheating: [the solution ↗️](https://www.wolframalpha.com/input?i=7+*+%281+-+%2860+choose+20%29%2F%2870+choose+20%29%29).

