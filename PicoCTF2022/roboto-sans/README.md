# Roboto Sans

> The flag is somewhere on this web application not necessarily on the website. Find it.

Roboto Sans first sounded like a font... But then I realised it might be a
reference to
[`robots.txt`](https://developers.google.com/search/docs/crawling-indexing/robots/intro).
And indeed, there's some curious stuff going on robots.txt:

```txt
User-agent *
Disallow: /cgi-bin/
Think you have seen your flag or want to keep looking.

ZmxhZzEudHh0;anMvbXlmaW
anMvbXlmaWxlLnR4dA==
svssshjweuiwl;oiho.bsvdaslejg
Disallow: /wp-admin/
```

The `wp-admin` and `cgi-bin` directories both 404. But the other text there
looks like Base64...

![](https://i.imgur.com/xC42Epi.png)
