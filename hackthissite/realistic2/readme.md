# Realistic missions: level 2

Simply inspecting the source reveals this line:

```html
<center><a href="/missions/realistic/2/update.php"><font color="#000000">update</font></a></center><br />
```

If we check out the `update.php` a login page is revealed. The most classic of all SQL injections seems to work fine:

* Username: `admin`
* Password: `abc" OR 1=1; -- `
