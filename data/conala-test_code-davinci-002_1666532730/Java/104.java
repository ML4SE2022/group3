public static List<Integer> sum(List<List<Integer>> lists) {
    List<Integer> result = new ArrayList<>();
    for (int i = 0; i < lists.get(0).size(); i++) {
        int sum = 0;
        for (List<Integer> list : lists) {
            sum += list.get(i);
        }
        result.add(sum);
    }
    return result;
}