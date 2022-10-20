Collections.sort(list, new Comparator<Map<String, Integer>>() {
    @Override
    public int compare(Map<String, Integer> o1, Map<String, Integer> o2) {
        int x1 = o1.get("x");
        int x2 = o2.get("x");
        if (x1 != x2) {
            return x1 - x2;
        }
        int y1 = o1.get("y");
        int y2 = o2.get("y");
        return y1 - y2;
    }
});