def d(n)
	(1..n/2).select{ |num| n % num == 0 }.reduce(:+) unless n == nil
end

def amicable?(a)
	b = d(a)
	d(b) == a && b != a
end

puts (0..10000).select{ |num| amicable?(num) }.reduce(:+)
