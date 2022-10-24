public static void main(String[] args) {
    List<String> list = Arrays.asList("a", "b", "c");
    List<List<String>> result = new ArrayList<>();
    permute(list, 0, result);
    System.out.println(result);
}

private static void permute(List<String> list, int start, List<List<String>> result) {
    if (start == list.size()) {
        result.add(new ArrayList<>(list));
    } else {
        for (int i = start; i < list.size(); i++) {
            Collections.swap(list, start, i);
            permute(list, start + 1, result);
            Collections.swap(list, start, i);
        }
    }
}