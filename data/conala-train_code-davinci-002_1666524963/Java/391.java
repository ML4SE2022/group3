Collections.sort(list, new Comparator<Tuple>() {
    @Override
    public int compare(Tuple o1, Tuple o2) {
        return o1.getKey().compareTo(o2.getKey());
    }
});