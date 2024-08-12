# Local Authority

> Can you get the flag?

This one is about client-side password validation using JavaScript. The credentials we enter are checked using the following code (from `/secure.js`, which is in the src-attribute of the script tag):

```js
function checkPassword(username, password) {
  if( username === 'admin' && password === 'strongPassword098765' )
  {
    return true;
  }
  else
  {
    return false;
  }
}

```

We get the flag when we enter these credentials: `picoCTF{j5_15_7r4n5p4r3n7_8086bcb1}`.
