public static int sum(int[] arr) {
    int sum = 0;
    for (int i = 0; i < arr.length; i++) {
        sum += Math.pow(arr[i], i);
    }
    return sum;
}