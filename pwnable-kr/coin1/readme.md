# Toddler's Bottle - coin1

> Mommy, I wanna play a game!
> (if your network response time is too slow, try nc 0 9007 inside pwnable.kr server)

The given explanation is quite clear:

<img width="1028" alt="image" src="https://user-images.githubusercontent.com/6025224/252155596-de56948b-376d-4395-923c-0542cefc710c.png">

This is clearly a perfect use case for a [binary search procedure](https://en.wikipedia.org/wiki/Binary_search_algorithm). We always know whether the counterfeit coin is within a given range, by checking if the total weight is divisible by 10.
Following Python code implements the binary search procedure and repeats it 100 times. It uses pwntools to handle the connection.

```py
from pwn import *
import re

p = remote("pwnable.kr", 9007)
p.recv()

for i in range(100):
    N, C = re.findall("N=(\d+) C=(\d+)", p.recv().decode("utf-8"))[0]
    N = int(N)
    C = int(C)

    start, end = 0, N-1
    while start <= end and C > 0:
        mid = (start + end) // 2
        x = bytes(" ".join([str(j) for j in range(start, mid+1)]), encoding="utf-8")
        p.sendline(x)
        result = int(p.recvline()[:-1])
        if result % 10 == 0: start = mid + 1
        else: end = mid - 1
        C -= 1

    while C > 0:
        p.sendline(b"0")
        p.recv(1024)
        C -= 1

    p.sendline(bytes(str(start), encoding="utf-8"))
    print(p.recv().decode("utf-8"))

print(p.recv().decode("utf-8"))
```

There was just one small inconvenience. Like the challenge mentioned, my network response times were too slow to reach the required 100 coins. So I logged in using the ssh-credentials of another challenge, changed the netcat address to `0` and ran the script "locally" instead. Luckily, pwntools was installed there too. The program just needed some small edits, as the Python version on their machine is still 2.x. This finally worked:

<img width="1247" alt="image" src="https://user-images.githubusercontent.com/6025224/252156839-4b6b093d-e00e-46d7-a58f-092e484ed3f6.png">