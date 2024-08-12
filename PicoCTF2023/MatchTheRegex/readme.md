# MatchTheRegex

> How about trying to match a regular expression? The website is running here.

The regular expression we're supposed to match is in a comment in the source code:

```
...
let val = document.getElementById("name").value;
// ^p.....F!?
fetch(`/flag?input=${val}`)
	.then(res => res.text())
...
```

Submitting `picoCTF` works.

