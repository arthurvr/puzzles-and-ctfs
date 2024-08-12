# Grotesque - sudoku

> Daddy likes to play sudoku and he is fairly good at it
>
> but sometimes he is too errogant :(
>
> lets challenge him!

Example gameplay:

```
$ nc pwnable.kr 9016                 

	---------------------------------------------------
	-              Shall we play a game?              -
	---------------------------------------------------
	
	Daddy likes to play sudoku (https://en.wikipedia.org/wiki/Sudoku)
	but he complains its too easy :( 
	Maybe I can give him more challenging sudoku by adding some 
	additional rules for each puzzle..

	Do you wanna try? :)
	
	- How to play -
	1. you get a sudoku puzzle and additional rule.
	2. you give me back a solution in JSON format 
	3. iterate 1-2 and beat stage 100 for flag.
	4. each stage has 5 second time limit.

	press enter to see example.
```
	
```
<example> 
---- Server Output (0 indicates blank) ----
Stage  1

[0, 4, 0, 9, 1, 3, 7, 0, 5]
[0, 1, 7, 0, 0, 0, 4, 0, 0]
[0, 0, 3, 8, 0, 7, 0, 0, 0]
[0, 2, 0, 0, 3, 0, 0, 9, 0]
[0, 8, 9, 1, 2, 0, 3, 0, 4]
[7, 0, 0, 5, 8, 9, 6, 0, 0]
[1, 0, 0, 2, 7, 0, 9, 4, 3]
[4, 7, 2, 3, 0, 0, 0, 5, 0]
[3, 0, 0, 4, 0, 0, 0, 1, 0]

- additional rule -
sum of the following numbers (at row,col) should be bigger than 23
(row,col) : (4,4)
(row,col) : (2,5)
(row,col) : (9,6)
(row,col) : (9,3)
solution? : 

---- Client Input(paste it without newline) ---- 
[[2,4,6,9,1,3,7,8,5],[8,1,7,6,5,2,4,3,9],
[9,5,3,8,4,7,1,6,2],[6,2,1,7,3,4,5,9,8],
[5,8,9,1,2,6,3,7,4],[7,3,4,5,8,9,6,2,1],
[1,6,8,2,7,5,9,4,3],[4,7,2,3,9,1,8,5,6],
[3,9,5,4,6,8,2,1,7]]

---- Server Output ----
cheking your solution...
correct!

	
press enter to start game
```

Ah, a challenge that's not about binary exploitation! I think this is just a programming exercise. Sudoku solvers are the basic example for a [Backtracking](https://en.wikipedia.org/wiki/Backtracking) algorithm, and 5 seconds per game is really workable. Including the additional rule is quite straight forward using backtracking. There's lots of open-source solvers already, but I wrote one myself: see `solution.py`.

