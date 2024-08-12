# Extended basics 10

> The following is a batch script authentication system. Your goal here is to get the batch script to authenticate you by inputting a password into the field. For this extbasic, your goal is to circumvent authentication altogether. Decrypting the password is for extbasic11.


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

Notice the way `%INPUT%` is used in the if-statement. The following input will bypass the check:

```powershell
"=="" set passwordvalue=1065435274 && goto :end abc
```

Where the last command doesn't matter: whatever makes the program crash will work.