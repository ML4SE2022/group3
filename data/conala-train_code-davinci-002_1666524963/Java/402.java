Collections.sort(list, new Comparator<List<Integer>>() {
    @Override
    public int compare(List<Integer> o1, List<Integer> o2) {
        if (o1.get(0) == o2.get(0)) {
            return o1.get(1) - o2.get(1);
        } else {
            return o1.get(0) - o2.get(0);
        }
    }
});