public static char mostFrequentChar(String s) {
    Map<Character, Integer> map = new HashMap<>();
    for (int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        if (map.containsKey(c)) {
            map.put(c, map.get(c) + 1);
        } else {
            map.put(c, 1);
        }
    }
    int max = 0;
    char maxChar = ' ';
    for (Map.Entry<Character, Integer> entry : map.entrySet()) {
        if (entry.getValue() > max) {
            max = entry.getValue();
            maxChar = entry.getKey();
        }
    }
    return maxChar;
}