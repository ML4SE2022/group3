Collections.sort(list, new Comparator<List<Integer>>() {
    @Override
    public int compare(List<Integer> o1, List<Integer> o2) {
        return o1.get(index).compareTo(o2.get(index));
    }
});