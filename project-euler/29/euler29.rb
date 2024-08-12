combinations = []

(2..100).each do |a|
	(2..100).each do |b|
		combinations.push(a**b)
	end
end

p combinations.uniq.length
