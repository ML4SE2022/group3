public static List<Integer> findAllPositionsOfMaxValue(List<Integer> list) {
    List<Integer> result = new ArrayList<>();
    int max = Integer.MIN_VALUE;
    for (int i = 0; i < list.size(); i++) {
        if (list.get(i) > max) {
            max = list.get(i);
            result.clear();
            result.add(i);
        } else if (list.get(i) == max) {
            result.add(i);
        }
    }
    return result;
}