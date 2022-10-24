public static void sort(List<List<String>> list, int... keys) {
    Collections.sort(list, new Comparator<List<String>>() {
        @Override
        public int compare(List<String> o1, List<String> o2) {
            for (int key : keys) {
                int cmp = o1.get(key).compareTo(o2.get(key));
                if (cmp != 0) {
                    return cmp;
                }
            }
            return 0;
        }
    });
}