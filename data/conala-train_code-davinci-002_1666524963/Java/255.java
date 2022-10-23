Map<String, Integer> map = new HashMap<>();
map.put("a", "1");
map.put("b", "2");
map.put("c", "3");

Map<String, Integer> result = map.entrySet().stream()
    .collect(Collectors.toMap(Map.Entry::getKey, e -> Integer.valueOf(e.getValue())));