public static <T> void sort(List<T> list, List<? extends Comparable<? super T>> order) {
    Map<T, Integer> index = new HashMap<T, Integer>();
    for (int i = 0; i < order.size(); i++) {
        index.put(order.get(i), i);
    }
    Collections.sort(list, new Comparator<T>() {
        @Override
        public int compare(T o1, T o2) {
            return index.get(o1) - index.get(o2);
        }
    });
}