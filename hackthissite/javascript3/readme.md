# Javascript missions: level 3

The following code is given:

```javascript
var foo = 5 + 6 * 7 
var bar = foo % 8
var moo = bar * 2
var rar = moo / 3
function check(x) {
	if (x.length == moo) {
		alert("win!");
		window.location += "?lvl_password="+x;
	} else {
		alert("fail D:");
	}
}
```

Simple math teaches us that `moo` will equal 14, so we input some string containing 14 characters.
