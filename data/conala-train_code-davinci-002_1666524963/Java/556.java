List<String> dates = new ArrayList<>();
Collections.sort(dates, new Comparator<String>() {
    @Override
    public int compare(String o1, String o2) {
        return o1.compareTo(o2);
    }
});