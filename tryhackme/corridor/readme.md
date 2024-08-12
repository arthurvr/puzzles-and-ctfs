# tryhackme.com: corridor

[Link](https://tryhackme.com/room/corridor)

### Escape the Corridor

> You have found yourself in a strange corridor. Can you find your way back to where you came?
>
> In this challenge, you will explore potential IDOR vulnerabilities. Examine the URL endpoints you access as you navigate the website and note the hexadecimal values you find (they look an awful lot like a hash, don't they?). This could help you uncover website locations you were not expected to access.

IDOR vulnerabilities are [Insecure Direct Object References](https://portswigger.net/web-security/access-control/idor).

As we're looking for hidden website locations, I immediately started dirbuster with a serious wordlist. This gave no results, so let's manually start digging for these hashes.

Let's start digging for said hashes in the website source code. The main page contains an image with a lot of doors. Using a `<map>`, the doors all link to a different page. The following are the links in the image `<map>` on the main page.

```
c4ca4238a0b923820dcc509a6f75849b
c81e728d9d4c2f636f067f89cc14862c
eccbc87e4b5ce2fe28308fd9f2a7baf3
a87ff679a2f3e71d9181a67b7542122c
e4da3b7fbbce2345d7772b0674a318d5
1679091c5a880faf6fb5e6087eb1b2dc
8f14e45fceea167a5a36dedd4bea2543
c9f0f895fb98ab9159f51fd0297e236d
45c48cce2e2d7fbdea1afc51c7c6ad26
d3d9446802a44259755d38e6d163e820
6512bd43d9caa6e02c990b0a82652dca
c20ad4d76fe97759aa27a0c99bff6710
c51ce410c124a10e0db5e4b97fc2af39
```

Those are MD5 hashes for the numbers 1 until 13. The links themselves all seem the same: empty rooms. So I decided to try room 14 and room 0? That's hashes `aab3238922bcc25a6f606eb525ffdc56` and `cfcd208495d565ef66e7dff9f98764da`.

Room 14 does not exist, but on room 0 I found the flag.
