n = ARGV.length == 1 ? ARGV[0].to_i : 3

s = 0
for x in 1 .. n
    for y in x + 1 .. n
        s += x.gcd(y)
    end
end

puts s