# Operation Oni

> Download the disk image, find the key and log into the remote machine.

Sounds like a job for [Autopsy](https://github.com/sleuthkit/autopsy). Autopsy is installed on Kali by default.

1. You control autopsy through a web app. Open the command line tool and click the link.
2. Then you have to create a new case first.
3. Then create a host, and add the image file.
4. Then click "analyze" one of the partitions. I always choose the biggest partition first, it's most likely to be the file system.
5. Click "file analysis"... now it's time to explore. Clicking "expand directories" on the left side gives a nice overview.
6. The root user has a `.ssh` directory!
7. Remember that after downloading the private key, you have to give it the right permissions to be able to use it to log in. SSH will complain when using a keyfile with broad permissions.

```
chmod 600 key_file
```

8. We can actually log in using this key file!

```
ssh -i key_file -p 59329 ctf-player@saturn.picoctf.net
```

9. The flag is in `flag.txt` in the home directory.
