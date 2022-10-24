Map<String, String> map = new HashMap<>();
map.put("A", "a");
map.put("B", "b");
map.put("C", "c");

Map<String, String> lowercaseMap = map.entrySet()
    .stream()
    .collect(Collectors.toMap(
        e -> e.getKey().toLowerCase(),
        e -> e.getValue().toLowerCase()
    ));