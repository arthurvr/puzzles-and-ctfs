# credstuff

> We found a leak of a blackmarket website's login credentials. Can you find the password of the user `cultiris` and successfully decrypt it?

> The first user in `usernames.txt` corresponds to the first password in `passwords.txt`. The second user corresponds to the second password, and so on.

The username we're looking for is on line 378. In the passwords file, I find

```
cvpbPGS{P7e1S_54I35_71Z3}
```

Looks like a flag indeed! The `{` character is untouched, so I immediately think about a ceasar cipher again... and again, [CyberChef](https://gchq.github.io/CyberChef) makes this too easy. 

![](https://i.imgur.com/OdRT5MG.png)
