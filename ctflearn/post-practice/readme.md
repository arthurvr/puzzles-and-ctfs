# POST Practice

> This website requires authentication, via POST. However, it seems as if someone has defaced our site. Maybe there is still some way to authenticate? http://165.227.106.113/post.php

The source code contains the admin+password combination we need to send:

```
<!-- username: admin | password: 71urlkufpsdnlkadsf -->
```

Let's use curl to craft the request:


```
~/c/c/post-practice ❯❯❯ curl -X POST -F 'username=admin' -F 'password=71urlkufpsdnlkadsf' http://165.227.106.113/post.php

<h1>flag{p0st_d4t4_4ll_d4y}</h1>
```

