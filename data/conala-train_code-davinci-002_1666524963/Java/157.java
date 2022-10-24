Collections.sort(list, new Comparator<int[]>() {
    @Override
    public int compare(int[] o1, int[] o2) {
        if (o1[0] != o2[0]) {
            return o2[0] - o1[0];
        } else {
            return o1[1] - o2[1];
        }
    }
});