# Cyber Security Challenge Belgium (Sample questions)

>  Writeup while solving the *Cyber Security Challenge Belgium* [sample questions](https://cybersecuritychallenge.be/ctf101) - Arthur Verschaeve

Disclaimer: these are really beginner level. These got me motivated to go find a team and participate this year though :)

## Challenge 1: S3cRet Adm1n P4nel

> Websites often get hacked, and it's often easier than you think. Why don't you try to get into our Super Secret Admin Panel? (This challenge contains 2 flags)

Typical SQL injection, right in the login GET request. I used SQLMap to obtain the two flags. (But the challenge breaks every now and then - I think it's simply broken.)

## Challenge 2: What is this gibberish?

> Programming can be pretty difficult sometimes, but figuring out what someone else's code does is often even more difficult. This is called reverse-engineering. Can you figure out what the script below does?

JSFuck is pretty famous by now :) It's easy once you recognise it, just google for a deobfuscation tool.

![](https://i.imgur.com/L9Uc1WL.png)

## Challenge 3: Encode ALL the stuff!

> Encoding and encryption are often used on the internet. This secret message underwent a few transformations. Can you figure out the original message?

> Free tip: Use [Cyberchef](https://gchq.github.io/CyberChef/)!

This CyberChef tool is cool. It allows you to stack multiple encoding layers onto eachother. We start with the given string:

```
NzAgNjYgNzAgN2IgNzAgNjUgNmMgNjMgNjcgNjIgNWYgNjggNjYgNzIgNzEgNWYgNjcgNjIgNWYgNmYgNzIgNWYgNzIgNmUgNjYgNmMgN2Q=
```

Which becomes this after decoding from Base64:

```
70 66 70 7b 70 65 6c 63 67 62 5f 68 66 72 71 5f 67 62 5f 6f 72 5f 72 6e 66 6c 7d
```

Pretty obvious those are hexadecimal ASCII characters, and indeed, it becomes:

```
pfp{pelcgb_hfrq_gb_or_rnfl}
```

Not quite what we want (yet), but it's starting to look like a flag. Because we know the flag should start with `csc{` (13 characters difference), let's try to ROT13 the result:

```
csc{crypto_used_to_be_easy}
``` 

![](https://i.imgur.com/VU2hhze.png)

## Challenge 4: I knew running Linux would come in handy one day!

> Even binaries can be picked apart. You'll have to run this binary on Linux and figure out the password.

Uhm, I don't think it's a great idea to just go run that binary without having a look at it first ;) Just running `strings` on it reveals the flag:

![](https://i.imgur.com/TdEyesQ.png)
