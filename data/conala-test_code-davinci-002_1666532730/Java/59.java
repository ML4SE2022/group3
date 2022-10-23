public static List<Integer> findNMaxDiff(List<Integer> list1, List<Integer> list2, int n) {
    List<Integer> result = new ArrayList<>();
    if (list1 == null || list2 == null || list1.size() != list2.size()) {
        return result;
    }
    int size = list1.size();
    int[] diff = new int[size];
    for (int i = 0; i < size; i++) {
        diff[i] = Math.abs(list1.get(i) - list2.get(i));
    }
    Arrays.sort(diff);
    for (int i = size - 1; i >= size - n; i--) {
        result.add(diff[i]);
    }
    return result;
}