import java.util.*;

public class LegendrePrimeCounter {
    public static void main(String[] args) {
        LegendrePrimeCounter counter = new LegendrePrimeCounter(1000000000);
        for (int i = 0, n = 1; i < 10; ++i, n *= 10)
            System.out.printf("10^%d\t%d\n", i, counter.primeCount((n)));
    }

    private List<Integer> primes;
    private Map<Integer, Map<Integer, Integer>> phiCache = new HashMap<>();

    public LegendrePrimeCounter(int limit) {
        primes = generatePrimes((int)Math.sqrt((double)limit));
    }

    public int primeCount(int n) {
        if (n < 2)
            return 0;
        int a = primeCount((int)Math.sqrt((double)n));
        return phi(n, a) + a - 1;
    }

    private int phi(int x, int a) {
        if (a == 0)
            return x;
        Map<Integer, Integer> map = phiCache.computeIfAbsent(x, k -> new HashMap<>());
        Integer value = map.get(a);
        if (value != null)
            return value;
        int result = phi(x, a - 1) - phi(x / primes.get(a - 1), a - 1);
        map.put(a, result);
        return result;
    }

    private static List<Integer> generatePrimes(int limit) {
        boolean[] sieve = new boolean[limit >> 1];
        Arrays.fill(sieve, true);
        for (int p = 3, s = 9; s < limit; p += 2) {
            if (sieve[p >> 1]) {
                for (int q = s; q < limit; q += p << 1)
                    sieve[q >> 1] = false;
            }
            s += (p + 1) << 2;
        }
        List<Integer> primes = new ArrayList<>();
        if (limit > 2)
            primes.add(2);
        for (int i = 1; i < sieve.length; ++i) {
            if (sieve[i])
                primes.add((i << 1) + 1);
        } 
        return primes;
    }
}