public static boolean allEqual(List<Integer> list) {
    return list.stream().distinct().limit(2).count() <= 1;
}