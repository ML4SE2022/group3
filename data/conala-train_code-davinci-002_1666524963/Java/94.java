public static int getClosest(List<Integer> list, int given) {
    int minDiff = Integer.MAX_VALUE;
    int number = 0;
    for (int num : list) {
        int diff = Math.abs(num - given);
        if (diff < minDiff) {
            minDiff = diff;
            number = num;
        }
    }
    return number;
}