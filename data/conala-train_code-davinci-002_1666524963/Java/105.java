Map<String, Integer> map = new HashMap<>();
for (String s : list) {
    map.put(s, map.getOrDefault(s, 0) + 1);
}