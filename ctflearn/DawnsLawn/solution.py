import numpy as np

# Map the different states of a square to a number, which is much easier to program :) 
num_map = {
    '.': 0,
    '_': 1,
    '\\': 2,
    '-': 3,
    '/': 4,
    '|': 5,
    '*': 6
}

# Fetch the given lawn
lawn_lines = open('given_lawn.txt', 'r').read().split('\n')
lawn = np.array([
    [num_map[i] for i in line] for line in lawn_lines
])

# Mowing:
lawn -= 2

# Grow, but don't grow on infertile land (those squares stay == 0)
dimension = len(lawn_lines[0])
grow = np.tile(np.arange(dimension - 1, -1, -1), (dimension, 1))
grow[lawn <= 0] = 0
lawn += grow

# Can't grow past a flower.
lawn[lawn >= 6] = 6

# Count the flowers
flowers_count = (lawn == 6).sum()
print("# Flowers:")
print(flowers_count)
