Map<String, Integer> map = new HashMap<>();
map.put("a", 1);
map.put("b", 2);
map.put("c", 3);

List<Map.Entry<String, Integer>> list = new ArrayList<>(map.entrySet());
list.sort(Map.Entry.comparingByValue());

for (Map.Entry<String, Integer> entry : list) {
    System.out.println(entry.getKey() + ": " + entry.getValue());
}