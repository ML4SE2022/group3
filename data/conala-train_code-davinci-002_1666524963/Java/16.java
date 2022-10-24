public static List<List<Integer>> getAllCombinations(List<Integer> list) {
    List<List<Integer>> result = new ArrayList<>();
    for (int i = 0; i < list.size(); i++) {
        for (int j = i + 1; j < list.size(); j++) {
            List<Integer> temp = new ArrayList<>();
            temp.add(list.get(i));
            temp.add(list.get(j));
            result.add(temp);
        }
    }
    return result;
}