Arrays.sort(array, new Comparator<Map<String, Object>>() {
    @Override
    public int compare(Map<String, Object> o1, Map<String, Object> o2) {
        return o1.get("name").toString().compareTo(o2.get("name").toString());
    }
});