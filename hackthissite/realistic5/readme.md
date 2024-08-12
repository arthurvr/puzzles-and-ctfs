# Realistic missions: level 5

The `robots.txt` file of this site contains a list of files the developers don't want us to see:

```
User-agent: *
Disallow: /lib
Disallow: /secret
```

This `/secret` directory contains two files: `admin.php` and `admin.bak.php`. The bak-file, generally meaning backup-file, contains the following:

```
error matching hash ad5011ff0b4a58c431b457d1eae8e1aa
```

This should be the hash of the password. If the technology is "about 10 years old", MD4 is the first hashing algorithm that comes to mind. Cracking it is easy using John the ripper:

```
$ john md4.txt --format=raw-md4
$ john md4.txt --show
```



