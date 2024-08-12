# Virtual Machine 0

> Can you crack this black box?

> We grabbed this design doc from enemy servers: Download. We know that the rotation of the red axle is input and the rotation of the blue axle is output. The following input gives the flag as output: Download.


I got a `.dae` file: a COLLADA 3D model. [Blender](https://www.blender.org/) can open these:

![](https://i.imgur.com/ri506eG.png)

I got a very simple gear train which was encapsulated in Lego bricks. After removing the Lego bricks, it looked like this:

![](https://i.imgur.com/gY5Pu16.png)

The small gear seems to have 8 teeth, the big one 40. That makes for a gear ratio of 5. Let's calculate what output the given input will give:

![](https://i.imgur.com/NUqFfKJ.png)

I converted the output number to hexadecimal, so I could covert it to a flag:

![](https://i.imgur.com/98hNlZf.png)
