Map<String, Integer> map = new HashMap<>();
map.put("a", 1);
map.put("b", 2);
map.put("c", 3);
map.put("d", 4);

List<Map.Entry<String, Integer>> list = new ArrayList<>(map.entrySet());
list.sort(Comparator.comparing(Map.Entry::getValue));
list.sort(Comparator.comparing(Map.Entry::getKey));