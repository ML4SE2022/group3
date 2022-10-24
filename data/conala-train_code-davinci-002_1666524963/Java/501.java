Map<String, Integer> map = new HashMap<>();
map.put("a", 1);
map.put("b", 2);
map.put("c", 3);
map.put("d", 4);

for (Map.Entry<String, Integer> entry : map.entrySet()) {
    if (entry.getValue() == 3) {
        System.out.println(entry.getKey());
    }
}