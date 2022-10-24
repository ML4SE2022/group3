public static int[] maxLength(List<List<String>> list) {
    int[] maxLength = new int[list.get(0).size()];
    for (List<String> row : list) {
        for (int i = 0; i < row.size(); i++) {
            maxLength[i] = Math.max(maxLength[i], row.get(i).length());
        }
    }
    return maxLength;
}