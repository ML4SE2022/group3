public static int max(int[] list, int length) {
    int max = list[0];
    for (int i = 1; i < length; i++) {
        if (list[i] > max) {
            max = list[i];
        }
    }
    return max;
}