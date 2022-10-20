Collections.sort(list, new Comparator<String>() {
    @Override
    public int compare(String o1, String o2) {
        return o1.split(" ")[1].compareTo(o2.split(" ")[1]);
    }
});