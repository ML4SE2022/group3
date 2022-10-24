Map<String, Integer> map = new HashMap<>();
map.put("a", 1);
map.put("b", 2);
map.put("c", 3);

int max = 0;
String maxKey = null;
for (Map.Entry<String, Integer> entry : map.entrySet()) {
    if (maxKey == null || entry.getValue() > max) {
        maxKey = entry.getKey();
        max = entry.getValue();
    }
}