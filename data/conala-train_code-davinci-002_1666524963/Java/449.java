public static List<Integer> add(List<Integer> a, List<Integer> b) {
    List<Integer> result = new ArrayList<>();
    for (int i = 0; i < a.size(); i++) {
        result.add(a.get(i) + b.get(i));
    }
    return result;
}