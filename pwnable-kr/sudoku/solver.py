import json
from pwn import *

class SudokuSolver:
    def __init__(self, board, constraint_cells, constraint_value, sumtotal):
        self.constraint_cells = constraint_cells
        self.constraint_value = constraint_value
        self.board = board
        self.sumtotal = sumtotal
        self.todo = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    self.todo.append((i, j)) 

    def verify(self, row, col):
        poss = [0 for _ in range(10)]
        for i in range(9):
            poss[self.board[i][col]] += 1
        del poss[0]
        if any(map(lambda x: x > 1, poss)):
            return False

        poss = [0 for _ in range(10)]
        for j in range(9):
            poss[self.board[row][j]] += 1
        del poss[0]
        if any(map(lambda x: x > 1, poss)):
            return False

        poss = [0 for _ in range(10)]
        bucket_i, bucket_j = (i // 3) * 3, (j // 3) * 3
        for bi in range(bucket_i, bucket_i + 3):
            for bj in range(bucket_j, bucket_j + 3):
                poss[self.board[bi][bj]] += 1
        del poss[0]
        return not any(map(lambda x: x > 1, poss))

    def verify_extra_constraint(self):
        sumtotal = 0
        for i, j in self.constraint_cells:
            sumtotal += self.board[i][j]
        return sumtotal > self.constraint_value if self.sumtotal == "larger" else sumtotal < self.constraint_value

    def encode_board(self):
        return str(json.dumps(self.board)).replace(' ', '').encode()

    def solve(self, which=0):
        if which == len(self.todo):
            return self.verify_extra_constraint()

        i, j = self.todo[which]
        for x in range(1, 10):
            self.board[i][j] = x
            if self.verify(i, j) and self.solve(which+1):
                return True
        self.board[i][j] = 0

def parse_output(out):
    board = []
    constraints = []
    constraint_value = None
    sumtotal = None
    for line in filter(len, out.split(b'\n')):
        if line[0] == ord('['):
            board.append(eval(line))
        elif line[0] == ord('('):
            constraints.append(eval(line.split(b':')[-1]))
        elif line.startswith(b'sum of the following'):
            constraint_value = eval(line.split()[-1])
            sumtotal = "larger" if b'bigger' in line else 'smaller'

    # Constraints should also be zero-indexed!
    constraints = [(i-1, j-1) for (i, j) in constraints]

    return board, constraints, constraint_value, sumtotal


p = remote('pwnable.kr', 9016)

p.sendline()
p.sendline()
p.recvuntil(b'press enter to start game')

for i in range(100):
    print(f'Starting stage {i}...')
    out = p.recvuntil(b'solution?')
    board, constraints, constraint_value, sumtotal = parse_output(out)
    initial_board = board.copy()

    s = SudokuSolver(board, constraints, constraint_value, sumtotal)
    s.solve()
    soln = s.encode_board() + b'\n'
    p.send(soln)

p.recvuntil(b'get your flag.\n')
print(p.recvline().decode('utf-8'))
