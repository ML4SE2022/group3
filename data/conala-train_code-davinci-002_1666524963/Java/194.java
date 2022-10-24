Collections.sort(list, new Comparator<List<String>>() {
    @Override
    public int compare(List<String> o1, List<String> o2) {
        return o1.get(index).compareTo(o2.get(index));
    }
});