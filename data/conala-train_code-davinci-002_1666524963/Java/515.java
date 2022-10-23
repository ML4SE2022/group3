Collections.sort(list, new Comparator<Tuple>() {
    @Override
    public int compare(Tuple o1, Tuple o2) {
        if (o1.getFirst() == o2.getFirst()) {
            return o1.getSecond().compareTo(o2.getSecond());
        }
        return o1.getFirst().compareTo(o2.getFirst());
    }
});