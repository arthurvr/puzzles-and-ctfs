existing_coins = [1, 2, 5, 10, 20, 50, 100, 200]
target_value = 200

# combinations[N] represents the different ways to get to value N.
# Logically combinations[0] = 1. The rest is calculated iteratively in the loop that follows.
combinations = [1] + [0] * target_value
for coin in existing_coins:
	for i in range(target_value + 1):
		if i >= coin:
			combinations[i] += combinations[i - coin]

print(combinations[target_value])
