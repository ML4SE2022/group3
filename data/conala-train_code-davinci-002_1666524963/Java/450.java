public static void main(String[] args) {
    List<String> tokens = Arrays.asList("a", "b", "c");
    List<String> result = new ArrayList<>();
    generateAllStrings(tokens, result, 0, "");
    System.out.println(result);
}

private static void generateAllStrings(List<String> tokens, List<String> result, int index, String current) {
    if (index == tokens.size()) {
        result.add(current);
        return;
    }
    generateAllStrings(tokens, result, index + 1, current + tokens.get(index));
    generateAllStrings(tokens, result, index + 1, current);
}