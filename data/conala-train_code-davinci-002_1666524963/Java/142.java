String str = "Hello World";
Map<Character, Integer> map = new HashMap<>();
for (char c : str.toCharArray()) {
    if (map.containsKey(c)) {
        map.put(c, map.get(c) + 1);
    } else {
        map.put(c, 1);
    }
}