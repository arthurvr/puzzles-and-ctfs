# timer

> You will find the flag after analysing this apk

I used a [decompiler](https://www.decompiler.com) that supports apk files, and found the following class inside `timer.apk/sources/com/example/timer/BuildConfig.java`:

```
public final class BuildConfig {
    public static final String APPLICATION_ID = "com.example.timer";
    public static final String BUILD_TYPE = "debug";
    public static final boolean DEBUG = Boolean.parseBoolean("true");
    public static final int VERSION_CODE = 1;
    public static final String VERSION_NAME = "picoCTF{t1m3r_r3v3rs3d_succ355fully_17496}";
}
```