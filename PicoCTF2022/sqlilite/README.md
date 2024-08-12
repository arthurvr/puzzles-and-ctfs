# SQLiLite

> Can you login to this website?

This is a basic SQL injection, don't even need SQLMap (or similar tools) for
this.

1. My first attempt reveals how to query is being constructed:

![](https://i.imgur.com/zJ038y3.png)

2. Bypass the conditions by putting `admin' or 1=1 --` in as username.

![](https://i.imgur.com/lnANQ8c.png)

3. The flag is hiding in the source code:

![](https://i.imgur.com/a7EORcT.png)


