# Javascript missions: level 7

The inline Javascript on this page performs the actual check:

```html
<button onclick="javascript:if (document.getElementById(&quot;pass&quot;).value==&quot;j00w1n&quot;){alert(&quot;You WIN!&quot;);window.location += &quot;?lvl_password=&quot;+document.getElementById(&quot;pass&quot;).value}else {alert(&quot;WRONG! Try again!&quot;)}">Check Password</button>
```

Let's rewrite the javascript code to make it a more readable:

```javascript
if (document.getElementById("pass").value=="j00w1n") {
	alert("You WIN!");
	window.location += "?lvl_password="+document.getElementById("pass").value
}
else {
	alert("WRONG! Try again!")
}
```

The password is clearly visible again.
