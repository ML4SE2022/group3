public static <T> Map<T, List<Tuple2<T, T>>> splitByFirst(List<Tuple2<T, T>> list) {
    Map<T, List<Tuple2<T, T>>> map = new HashMap<>();
    for (Tuple2<T, T> tuple : list) {
        List<Tuple2<T, T>> subList = map.get(tuple.getFirst());
        if (subList == null) {
            subList = new ArrayList<>();
            map.put(tuple.getFirst(), subList);
        }
        subList.add(tuple);
    }
    return map;
}