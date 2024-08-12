# Fresh Java

> Can you get the flag? Reverse engineer this Java program.

Ghidra's Java decompiler to the rescue. It spits out the following code (which contains the flag in all the if-statements):

```java
void main_java.lang.String[]_void(String[] param1)

{
  PrintStream pPVar1;
  String objectRef;
  int iVar2;
  char cVar3;
  Scanner objectRef_00;
  
  objectRef_00 = new Scanner(System.in);
  pPVar1 = System.out;
  pPVar1.println("Enter key:");
  objectRef = objectRef_00.nextLine();
  iVar2 = objectRef.length();
  if (iVar2 != 0x22) {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(0x21);
  if (cVar3 != '}') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(0x20);
  if (cVar3 != 'd') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(0x1f);
  if (cVar3 != '0') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(0x1e);
  if (cVar3 != 'a') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(0x1d);
  if (cVar3 != '1') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(0x1c);
  if (cVar3 != 'e') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(0x1b);
  if (cVar3 != 'f') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(0x1a);
  if (cVar3 != 'b') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(0x19);
  if (cVar3 != '2') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(0x18);
  if (cVar3 != '_') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(0x17);
  if (cVar3 != 'd') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(0x16);
  if (cVar3 != '3') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(0x15);
  if (cVar3 != 'r') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(0x14);
  if (cVar3 != '1') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(0x13);
  if (cVar3 != 'u') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(0x12);
  if (cVar3 != 'q') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(0x11);
  if (cVar3 != '3') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(0x10);
  if (cVar3 != 'r') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(0xf);
  if (cVar3 != '_') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(0xe);
  if (cVar3 != 'g') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(0xd);
  if (cVar3 != 'n') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(0xc);
  if (cVar3 != '1') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(0xb);
  if (cVar3 != 'l') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(10);
  if (cVar3 != '0') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(9);
  if (cVar3 != '0') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(8);
  if (cVar3 != '7') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(7);
  if (cVar3 != '{') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(6);
  if (cVar3 != 'F') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(5);
  if (cVar3 != 'T') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(4);
  if (cVar3 != 'C') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(3);
  if (cVar3 != 'o') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(2);
  if (cVar3 != 'c') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(1);
  if (cVar3 != 'i') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  cVar3 = objectRef.charAt(0);
  if (cVar3 != 'p') {
    pPVar1 = System.out;
    pPVar1.println("Invalid key");
    return;
  }
  pPVar1 = System.out;
  pPVar1.println("Valid key");
  return;
}
```

There are countless ways to get the actual flag out, I used vim macros :)


```java
picoCTF{700l1ng_r3qu1r3d_2bfe1a0d}
```

Which currently doesn't work on the website. I need to come back later - I believe this is just a mistake at the PicoCTF side... 
