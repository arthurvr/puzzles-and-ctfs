fibs = [1, 1]

while fibs.last.to_s.length < 1000
	fibs.push(fibs[-1] + fibs[-2])
end

# The `+1` is just there because arrays are zero-indexed
puts fibs.index(fibs.last) + 1
