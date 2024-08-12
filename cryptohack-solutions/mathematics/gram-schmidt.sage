A = matrix([[4,1,3,-1],
            [2,1,-3,4],
            [1,0,-2,7],
            [6, 2, 9, -5]])

GS = A.gram_schmidt()
solution = GS[0][3][1]
rounded_solution = round(solution, 5)

print(rounded_solution)
