public static void main(String[] args) {
    int[] arr = new int[100];
    for (int i = 0; i < arr.length; i++) {
        arr[i] = i;
    }
    shuffleArray(arr);
    for (int i = 0; i < 10; i++) {
        System.out.println(arr[i]);
    }
}

// Implementing Fisher–Yates shuffle
static void shuffleArray(int[] ar) {
    Random rnd = ThreadLocalRandom.current();
    for (int i = ar.length - 1; i > 0; i--) {
        int index = rnd.nextInt(i + 1);
        // Simple swap
        int a = ar[index];
        ar[index] = ar[i];
        ar[i] = a;
    }
}