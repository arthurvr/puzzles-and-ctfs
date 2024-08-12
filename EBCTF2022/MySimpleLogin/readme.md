# _MySimpleLogin_ Write-up

> I created my own secure Android application. Can you find the flag?


I decompiled the given APK using Jadx. Judging by the class name, `MainActivity.java` is the logical entry point. This can be confirmed in `AndroidManifest.xml`.

This function is key:

```java
public void checkPassword() {
    String i = this.edtPassword.getText().toString();
    String s = getResources().getString(R.string.OO0O00OOO00O0O);
    String h = getResources().getString(R.string.OO0O00OOO00OOO);
    String f = getResources().getString(R.string.OO0O0O0OO00OOO);
    String w = getResources().getString(R.string.OO0O0OOOO00OOO);
    if (l(String.valueOf(s) + i).equals(h)) {
        showError(w);
    } else {
        showFlag(f);
    }
}
```

So, `i` is whatever we enter as password.

The strings that are being looked up for `s`, `h`, `f` and `w` are in `res/values/strings.xml`:

```xml
<string name="OO0O0O0OO00OOO">Wrong Password! Try Again!</string>
<string name="OO0O00OOO00O0O">S3kuritY!</string>
<string name="OO0O00OOO00OOO">7f03e614c9f1c1a0561f87f33d83e599</string>
<string name="OO0O0OOOO00OOO">&gt;49s?#kjllw&gt;ijvnra;;i&gt;=kuki`ta;`iirj9::xtm;&lt;rij%</string>
```

Now, what does function `l(String.valueOf(s) + i)` do? It calculates an MD5 hash of `String.valueOf(s) + i`.

```java
public String l(String s) {
    try {
        MessageDigest digest = MessageDigest.getInstance("MD5");
        digest.update(s.getBytes());
        byte[] messageDigest = digest.digest();
        StringBuilder hexString = new StringBuilder();
        for (byte aMessageDigest : messageDigest) {
            String h = Integer.toHexString(aMessageDigest & 255);
            while (h.length() < 2) {
                h = "0" + h;
            }
            hexString.append(h);
        }
        return hexString.toString();
    } catch (NoSuchAlgorithmException e) {
        e.printStackTrace();
        return "";
    }
}
```

The strange thing though: if the calculated hash matches `h`...  `showError` is called. Odd! Although, looking at `showError` itself, it is clear that the function name is an obfuscation attempt. The function does the following:

```java
public void showError(String e) {
    this.lblPassword.setText(x(r(r(r(r(r(r(r(e, "r"), "s"), "t"), "u"), "v"), "w"), "x"), "X"));
}
```

With `r` and `x` more obfuscation:

```java
public String r(String s, String c) {
    return s.replace(c, "");
}
```

```java
public String x(String s, String k) {
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < s.length(); i++) {
        sb.append((char) (s.charAt(i) ^ k.charAt(i % k.length())));
    }
    return sb.toString();
}
```

I replicated these functions and threw in the input string found in the XML file:

```java
public class MainActivity {
    public static String x(String s, String k) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            sb.append((char) (s.charAt(i) ^ k.charAt(i % k.length())));
        }
        return sb.toString();
    }

    public static String r(String s, String c) {
        return s.replace(c, "");
    }

    public static void main(String[] args) {
        String e = ">49s?#kjllw>ijvnra;;i>=kuki`ta;`iirj9::xtm;<rij%";
        System.out.println(x(r(r(r(r(r(r(r(e, "r"), "s"), "t"), "u"), "v"), "w"), "x"), "X"));
    }
}
```

And executing this, I got the flag:

```
flag{3244f1269cc1fe33189c8112abb5cd12}
```
