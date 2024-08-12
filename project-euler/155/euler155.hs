-- Gotta admit, I probably made this a little too easy. However, I did learn something! The following paper
-- is a really good read on a very, very related problem: https://www.ias.ac.in/article/fulltext/reso/017/05/0468-0475.
--
-- Swapping series/parallel rules (resistors <-> caps) does not change the amount of solutions...

exactlyNlist = [1, 2, 4, 8, 20, 42, 102, 250, 610, 1486, 3710, 9228, 23050, 57718, 145288, 365820, 922194, 2327914, 5885800, 14890796, 37701452, 95550472, 242325118, 614869792, 1561228066]

main = print . sum $ take 18 exactlyNlist
