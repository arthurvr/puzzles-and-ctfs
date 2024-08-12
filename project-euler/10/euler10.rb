require 'prime'

# Lol, ruby makes this a little too easy :D
puts Prime.each(2_000_000).reduce(:+)
