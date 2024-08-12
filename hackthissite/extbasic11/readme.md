# Extended basics 11

> The following is a batch script authentication system. Your goal here is to get the batch script to authenticate you by inputting a password into the field.

```powershell
@ECHO OFF
SETLOCAL ENABLEDELAYEDEXPANSION
SET PRIME=2  3  5  7  11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101
SET CHARS=a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z
SET PASSWORDVALUE=1
SET INPUT=
SET /P INPUT=Insert password:
IF "%INPUT%"=="" "%~0"
ECHO Authenticating...
:OVERLOOP
SET CURRENTPOSITION=0
:SUBLOOP
IF /I "!INPUT:~%CHARACTERPOSITION%,1!"=="!CHARS:~%CURRENTPOSITION%,1!" SET /A PASSWORDVALUE*=!PRIME:~%CURRENTPOSITION%,3!
SET /A CURRENTPOSITION+=3
IF NOT %CURRENTPOSITION%==78 GOTO :SUBLOOP
SET /A CHARACTERPOSITION+=1
IF NOT "!INPUT:~%CHARACTERPOSITION%,1!"=="" GOTO :OVERLOOP
:END
ENDLOCAL&IF NOT %PASSWORDVALUE%==1065435274 GOTO :ACCESSDENIED
ECHO You have been authenticated. Welcome aboard!
GOTO :SILENTPAUSE
:ACCESSDENIED
ECHO Access denied!
:SILENTPAUSE
PAUSE > NUL
```

The script is multiplying prime numbers until the result is 1065435274. However, there is a catch: the result is 1065435274 mod 2^32, not exactly 1065435274. I wrote a python script to figure out the prime factors, and thus the letters used in the password. This script is in `solution.py`.

![](https://i.imgur.com/dYecXzM.png)

Then we simply have to guess I'm afraid. It's `logarithm` :)