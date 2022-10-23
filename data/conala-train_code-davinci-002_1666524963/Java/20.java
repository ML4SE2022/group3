public static <T> List<Set<T>> removeDuplicates(List<Set<T>> list) {
    List<Set<T>> result = new ArrayList<>();
    for (Set<T> set : list) {
        if (!result.contains(set)) {
            result.add(set);
        }
    }
    return result;
}