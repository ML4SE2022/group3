public static List<List<String>> parse(String s) {
    List<List<String>> result = new ArrayList<>();
    List<String> current = new ArrayList<>();
    int i = 0;
    while (i < s.length()) {
        if (s.charAt(i) == '[') {
            result.add(current);
            current = new ArrayList<>();
            i++;
        } else if (s.charAt(i) == ']') {
            i++;
        } else {
            int j = i;
            while (j < s.length() && s.charAt(j) != '[' && s.charAt(j) != ']') {
                j++;
            }
            current.add(s.substring(i, j));
            i = j;
        }
    }
    return result;
}