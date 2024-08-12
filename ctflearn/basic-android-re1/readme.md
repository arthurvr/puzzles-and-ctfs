# Basic Android RE 1

>  A simple APK, reverse engineer the logic, recreate the flag, and submit!

I did not have an Android APK decompiling tool on my laptop so used [an online one](http://www.javadecompilers.com/). The interesting file is `MainActivity.java`, which contains the following:

```java
package com.example.secondapp;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import org.apache.commons.codec.digest.DigestUtils;

public class MainActivity extends AppCompatActivity {
    /* access modifiers changed from: protected */
    public void onCreate(Bundle bundle) {
        super.onCreate(bundle);
        setContentView((int) C0272R.layout.activity_main);
    }

    public void submitPassword(View view) {
        EditText editText = (EditText) findViewById(C0272R.C0274id.editText2);
        if (DigestUtils.md5Hex(editText.getText().toString()).equalsIgnoreCase("b74dec4f39d35b6a2e6c48e637c8aedb")) {
            ((TextView) findViewById(C0272R.C0274id.textView)).setText("Success! CTFlearn{" + editText.getText().toString() + "_is_not_secure!}");
        }
    }
}
```

So we need to find out what string hashes to `b74dec4f39d35b6a2e6c48e637c8aedb` using MD5. There's [sites online](https://md5.gromweb.com/?md5=b74dec4f39d35b6a2e6c48e637c8aedb) that keep huge rainbow tables, and apparently this reverses to `Spring2019`. That would make the resulting flag:

```
CTFlearn{Spring2019_is_not_secure!}
```

Which I didn't even need to execute the code for :)
