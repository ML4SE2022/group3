public static void main(String[] args) {
    List<Integer> list = Arrays.asList(1, -1, 2, -2, 3, -3, 4, -4, 5, -5);
    Collections.sort(list, new Comparator<Integer>() {
        @Override
        public int compare(Integer o1, Integer o2) {
            if (o1 < 0 && o2 < 0) {
                return o2 - o1;
            } else if (o1 < 0) {
                return 1;
            } else if (o2 < 0) {
                return -1;
            } else {
                return o1 - o2;
            }
        }
    });
    System.out.println(list);
}