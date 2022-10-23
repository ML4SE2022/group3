public static List<Integer> removeDuplicates(List<Integer> list) {
    List<Integer> result = new ArrayList<>();
    for (int i = 0; i < list.size(); i++) {
        if (i == 0 || list.get(i) != list.get(i - 1)) {
            result.add(list.get(i));
        }
    }
    return result;
}