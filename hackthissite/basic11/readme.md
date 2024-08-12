# Basic missions: basic 11

There's this hint in the source code:

```
<!-- We even have our own collection - if you could find it! -->
```

The site seems to be vulnerable to one of the most common server-side misconfigurations: open directory listings. 

![](https://imgur.com/b20156fc-a4a9-044e-88b6-4325735323c2)

Besides that, we can access the Apache configuration file (`.htaccess`) in this directory. It gives away the location of the answer:

```
IndexIgnore DaAnswer.* .htaccess
<Files .htaccess>
require all granted
</Files>
```

Accessing that url (`https://www.hackthissite.org/missions/basic/11/e/l/t/o/n/DaAnswer/`) indeed gives us the answer (and a really bad pun):

```
The answer is short! Just look a little harder.
```

