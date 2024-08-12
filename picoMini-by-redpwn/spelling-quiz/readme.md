# spelling-quiz

> I found the flag, but my brother wrote a program to encrypt all his text files. He has a spelling quiz study guide too, but I don't know if that helps.

The given encryption program seems like a simple substitution cipher on the letters of the alphabet. I used a [frequency analysis](https://en.wikipedia.org/wiki/Letter_frequency) assuming the words in the study guide are english.

I used `count.py` to count the letter frequencies, which gave me the following result:

```
{'a': 206355, 'b': 96529, 'c': 205401, 'd': 66435, 'e': 14940, 'f': 76513, 'g': 17173, 'h': 3251, 'i': 214772, 'j': 4794, 'k': 11862, 'l': 162351, 'm': 90628, 'n': 131465, 'o': 107082, 'p': 27458, 'q': 57699, 'r': 311363, 's': 87009, 't': 216936, 'u': 49432, 'v': 198197, 'w': 270080, 'x': 239284, 'y': 30493, 'z': 8354}
```

We now know that `e` is the most common letter in English words, `a` is next, ... I used [quipquip](https://www.quipqiup.com) and only used the most frequent letters as a clue, quipquip figured out the rest. The result is

```
perhaps_the_dog_jumped_over_was_just_tired
```

Which is the correct flag (just add `picoCTF{ ... }`).
