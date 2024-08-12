# Extended basics 14

> Sam was trying to make a program to show how 1337 he is. But the output isn't always correct. Help him fix his program so he can impress his friends.

```java
package org.hackthissite.missions.extbasic;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class ExtBasic14 {

        private final ExecutorService executorService = Executors.newFixedThreadPool(100);
        private static final int MAX = 1337;
        private int timeToGetLeet = 0;

        ExtBasic14() throws InterruptedException {
                for (int i = 0; i < MAX; i++) {
                        executorService.execute(new Runnable() {
                                public void run() {
                                        incrementLeetness();
                                }
                        });
                }
                executorService.shutdown();
                while (!executorService.isTerminated()) {
                        Thread.sleep(500);
                }
                System.out.println(timeToGetLeet);
        }

        private void incrementLeetness() {
                int obfusticatedIncremental = timeToGetLeet;
                obfusticatedIncremental = obfusticatedIncremental + 1;
                timeToGetLeet = obfusticatedIncremental;
        }

        /**
         * @param args
         */
        public static void main(String[] args) throws InterruptedException {
                new ExtBasic14();
        }

}
```

I don't have much experience writing multithreaded code in Java. However, after some googling I started notificing the `synchronized` keyword a lot.

> synchronized methods enable a simple strategy for preventing thread interference and memory consistency errors: if an object is visible to more than one thread, all reads or writes to that object's variables are done through synchronized methods.

Hmm, looks like the `incremenetLeetness()` method needs to be synchronised? 

```java
        private synchronized void incrementLeetness() {
```