# WPA-ing Out

> I thought that my password was super-secret, but it turns out that passwords passed over the AIR can be CRACKED, especially if I used the same wireless network password as one in the `rockyou.txt` credential dump.


Just download rockyou from one of the many sites that host it. Then use this awesome tool called [aircrack-ng](https://github.com/aircrack-ng/aircrack-ng).

```
$ aircrack-ng -w rockyou.txt wpa-ing_out.pcap
```

![](https://i.imgur.com/SVkzqbD.png)

