public class FirstLastBits {

    // most significant set bit
    public static int mssb(int x) {
        return Integer.highestOneBit(x);
    }

    public static long mssb(long x) {
        return Long.highestOneBit(x);
    }

    public static int mssb_idx(int x) {
        return Integer.SIZE - 1 - Integer.numberOfLeadingZeros(x);
    }

    public static int mssb_idx(long x) {
        return Long.SIZE - 1 - Long.numberOfLeadingZeros(x);
    }

    public static int mssb_idx(BigInteger x) {
	return x.bitLength() - 1;
    }

    // least significant set bit
    public static int lssb(int x) {
        return Integer.lowestOneBit(x);
    }

    public static long lssb(long x) {
        return Long.lowestOneBit(x);
    }

    public static int lssb_idx(int x) {
        return Integer.numberOfTrailingZeros(x);
    }

    public static int lssb_idx(long x) {
        return Long.numberOfTrailingZeros(x);
    }

    public static int lssb_idx(BigInteger x) {
	return x.getLowestSetBit();
    }

    public static void main(String[] args) {
        System.out.println("int:");
        int n1 = 1;
        for (int i = 0; ; i++, n1 *= 42) {
            System.out.printf("42**%d = %10d(x%08x): M x%08x(%2d) L x%03x(%2d)\n",
                              i, n1, n1,
                              mssb(n1), mssb_idx(n1),
                              lssb(n1), lssb_idx(n1));
            if (n1 >= Integer.MAX_VALUE / 42)
                break;
        }
        System.out.println();
        System.out.println("long:");
        long n2 = 1;
        for (int i = 0; ; i++, n2 *= 42) {
            System.out.printf("42**%02d = %20d(x%016x): M x%016x(%2d) L x%06x(%2d)\n",
                              i, n2, n2,
                              mssb(n2), mssb_idx(n2),
                              lssb(n2), lssb_idx(n2));
            if (n2 >= Long.MAX_VALUE / 42)
                break;
        }
	System.out.println();
	System.out.println("BigInteger:");
	BigInteger n3 = BigInteger.ONE;
	BigInteger k = BigInteger.valueOf(1302);
	for (int i = 0; i < 10; i++, n3 = n3.multiply(k)) {
	    System.out.printf("1302**%02d = %30d(x%28x): M %2d L %2d\n",
			      i, n3, n3,
			      mssb_idx(n3),
			      lssb_idx(n3));
	}
    }
}