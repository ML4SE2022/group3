public static <T> List<List<T>> allCombinations(List<List<T>> lists) {
    List<List<T>> result = new ArrayList<>();
    allCombinations(lists, 0, new ArrayList<>(), result);
    return result;
}

private static <T> void allCombinations(List<List<T>> lists, int depth, List<T> current, List<List<T>> result) {
    if (depth == lists.size()) {
        result.add(current);
        return;
    }
    for (T element : lists.get(depth)) {
        List<T> copy = new ArrayList<>(current);
        copy.add(element);
        allCombinations(lists, depth + 1, copy, result);
    }
}