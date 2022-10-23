public static List<Pair<String, Integer>> map(String s) {
    List<Pair<String, Integer>> result = new ArrayList<>();
    for (int i = 0; i < s.length(); i++) {
        result.add(new Pair<>(s.substring(i, i + 1), i));
    }
    return result;
}