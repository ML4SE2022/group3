public static List<String> splitString(String s) {
    List<String> result = new ArrayList<>();
    int i = 0;
    while (i < s.length()) {
        int j = i + 1;
        while (j < s.length() && s.charAt(j) == s.charAt(i)) {
            j++;
        }
        result.add(s.substring(i, j));
        i = j;
    }
    return result;
}