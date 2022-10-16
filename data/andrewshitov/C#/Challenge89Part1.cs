using System;
using System.Numerics;

class Program {
    static int Main(string[] args)
    {
        int n = 3;
        if (args.Length == 1) n = int.Parse(args[0]);
        
        var s = new BigInteger(0);
        for (int x = 1; x <= n; x++) {
            for (int y = x + 1; y <= n; y++) {
                s += BigInteger.GreatestCommonDivisor(x, y);
            }
        }
        
        System.Console.WriteLine(s);

        return 0;
    }
}