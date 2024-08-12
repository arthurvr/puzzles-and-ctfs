# Shad3's Keyg3n_M1#1

> It's easy to break me! I want you to keygen me.

Found this challenge [here](https://crackmes.one/crackme/5e66aea233c5d4439bb2dde8).

## Solution

Let's have a look what file we got first:

![](https://i.imgur.com/siq9iVz.png)

IDA immediately drops us in the main program. Looks like there's a `scanf`-call (reading characters as input) immediately followed by a call to a `check_key` function... that makes sense.

![](https://i.imgur.com/x5tBWLv.png)

The graph view makes that `check_key` function very clear:

![](https://i.imgur.com/VEVqC6Y.png)

Let's see what's happening:

* `strlen` is called, and the result is compared to 7. Looks like the key length should be over 7.
* `strlen` is called again, and the result is compared to `0xA`. Looks like the key length should not be over 10.
* The next part is a loop. Notice the very typical loop counter that always gets increased by one. Looks like every character in the given key is read, and summed. It looks like the sum of the ASCII characters in the given key should be equal to a greater than 1000.

I came up manually with a key like this: `zzzzzzzzz`. This is 9 characters long. The ASCII value for a z-character is 122, and 122 times 9 is 1098. This seems to work! And indeed, it does not work with the a-character as 97 x 9 is less than 1000.

![](https://i.imgur.com/Bm0eR8m.png)

A possible keygen in Python looks like this:

```python
# This (very simple) keygen just generates random keys that pass the checks.

# This could be made a lot more efficient, and it could also actually generate
# valid keys instead of trying random ones... but this should work for almost
# all practical use cases :))

import random
import string

# Not including special characters or uppercase letters... Those will make for small sums as they're low ASCII values.
possible_chars = list(string.ascii_lowercase + string.digits)
def char_sum(s):
    result = 0
    for char in s:
        result += ord(char)
    return result

def pass_check(s):
    if len(s) <=7 or len(s)>=11: return False
    return char_sum(s) >= 1000

necessary_keys = 10
for i in range(necessary_keys):
    poss = ""
    while not pass_check(poss):
        desired_len = random.choice([8, 9, 10])
        poss = ''.join(random.choice(possible_chars) for i in range(desired_len))
    print(poss)
```
