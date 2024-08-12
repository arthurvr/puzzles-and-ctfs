p = 29;
ints = [14; 6; 11];

for i = [1: p]
  num = mod(i*i, p);
  if ismember(num, ints)
    i                          # This is the square root we're looking  for!
    p
  endif
end

