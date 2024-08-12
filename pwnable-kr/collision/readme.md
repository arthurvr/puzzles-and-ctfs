# Toddler's Bottle - collision

> Daddy told me about cool MD5 hash collision today.
> I wanna do something like that too!

Again, carefully inspecting the source code is important. 

<img width="842" alt="image" src="https://user-images.githubusercontent.com/6025224/251632444-cd866b9a-5491-4ab2-8a8f-7cd041497f0a.png">

The payload clearly has to be 20 bytes long. Five four-byte numbers are added together, and must make a sum of `0x21DD09EC`. This number itself is not divisible by 5, but we can write it as 4 times some number, plus a remainder! 

<img width="842" alt="image" src="https://user-images.githubusercontent.com/6025224/251632179-2509cb8f-c3c2-4e89-bd25-5c96ff081fad.png">

This indeed gets us the flag:

<img width="842" alt="image" src="https://user-images.githubusercontent.com/6025224/251632285-a479433d-8eee-481d-920d-b13e8a05d296.png">
