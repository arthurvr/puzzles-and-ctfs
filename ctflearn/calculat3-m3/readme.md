# Calculat3 M3 

> Here! http://web.ctflearn.com/web7/ I forget how we were doing those calculations, but something tells me it was pretty insecure.

This is a classic command injection vulnerability. Instead of a calculation, enter `; ls`, to list the files. You can do this using curl, burp suite, ... or just within your browser if you use devtools to remove the `readonly` attribute on the input tag.
