# Basic missions: basic 7

The calendar output is typical for the UNIX `cal` command, so we try a [command injection attack](https://owasp.org/www-community/attacks/Command_Injection). This seems to work. We can discover the location of the file by entering `2020 && ls` and can read it by simply accessing it using a browser.
