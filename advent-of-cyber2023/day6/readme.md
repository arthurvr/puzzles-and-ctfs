# Day 6: Memories of Christmas Past

* **If the coins variable had the in-memory value in the image below, how many coins would you have in the game?** 0x53504f4f = 1397772111.

![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5ed5961c6276df568891c3ea/room-content/7a9e27b711b796a812ea822aa072dc50.png)

* **What is the value of the final flag?** First get yourself 16 coins (this was annoying as it takes a while). Then go to the green figure and enter `aaaaaaaaaaaaffff` as name to get a near-infinite amount of coins. Repeat that but now enter `aaaabbbbccccddddeeeeffffgggghhhhhiiiiijjjjkkkkd` as name to overwrite the inventory. This `d` character is the ID of the star. After this, interact with the tree to get the flag

![](solution.png)