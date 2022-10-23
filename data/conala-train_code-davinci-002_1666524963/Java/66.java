public static boolean isSubset(List<Integer> list, List<Integer> sublist) {
    return sublist.stream().allMatch(list::contains);
}