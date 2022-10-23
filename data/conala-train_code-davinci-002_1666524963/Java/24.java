Arrays.sort(array, new Comparator<int[]>() {
    @Override
    public int compare(int[] o1, int[] o2) {
        return Integer.compare(o1[0], o2[0]);
    }
});