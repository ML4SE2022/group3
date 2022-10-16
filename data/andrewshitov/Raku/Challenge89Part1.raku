my $n = @*ARGS[0] // 3;

say [+] (1..$n).combinations(2).map: {[gcd] $_};