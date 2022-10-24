List<Integer> list = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
List<Tuple2<Integer, Integer>> pairs = new ArrayList<>();
for (int i = 0; i < list.size() - 1; i++) {
    if (list.get(i) % 2 == 0 && list.get(i + 1) % 2 == 0) {
        pairs.add(new Tuple2<>(list.get(i), list.get(i + 1)));
    }
}