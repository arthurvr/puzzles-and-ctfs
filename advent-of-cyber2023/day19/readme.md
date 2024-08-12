# Day 19: CrypTOYminers Sing Volala-lala-latility

This is an exercise on memory forensics using [volatility](https://github.com/volatilityfoundation/volatility). The walkthrough text by THM is very comprehensive, simply following the commands there got me all the answers. In summary:

```
$ cd ~/Desktop/Evidence/
$ cp Ubuntu_5.4.0-163-generic_profile.zip ~/.local/lib/python2.7/site-packages/volatility/plugins/overlays/linux/

$ vol.py -f linux.mem --profile="LinuxUbuntu_5_4_0-163-generic_profilex64" -h
$ vol.py -f linux.mem --profile="LinuxUbuntu_5_4_0-163-generic_profilex64" linux_bash
$ vol.py -f linux.mem --profile="LinuxUbuntu_5_4_0-163-generic_profilex64" linux_pslist

$ mkdir extracted

$ vol.py -f linux.mem --profile="LinuxUbuntu_5_4_0-163-generic_profilex64" linux_procdump -D extracted -p 10280
$ vol.py -f linux.mem --profile="LinuxUbuntu_5_4_0-163-generic_profilex64" linux_procdump -D extracted -p 10291

$ md5sum extracted/miner.10280.0x400000   
$ md5sum extracted/mysqlserver.10291.0x400000

$ vol.py -f linux.mem --profile="LinuxUbuntu_5_4_0-163-generic_profilex64" linux_enumerate_files | grep -i cron 
$ vol.py -f linux.mem --profile="LinuxUbuntu_5_4_0-163-generic_profilex64" linux_find_file -i 0xffff9ce9b78280e8 -O extracted/elfie
$ cat extracted/elfie
```

* **What is the exposed password that we find from the bash history output?** `NEhX4VSrN7sV`
* **What is the PID of the miner process that we find?** 10280
* **What is the MD5 hash of the miner process?** `153a5c8efe4aa3be240e5dc645480dee`
* **What is the MD5 hash of the mysqlserver process?** `c586e774bb2aa17819d7faae18dad7d1`
* **Use the command strings `extracted/miner.10280.0x400000 | grep http://`. What is the suspicious URL? (Fully defang the URL using CyberChef)** `hxxp[://]mcgreedysecretc2[.]thm`
* **After reading the elfie file, what location is the mysqlserver process dropped in on the file system?** `/var/tmp/.system-python3.8-Updates/mysqlserver`
