Map<String, String> map = new HashMap<>();
map.put("key1", "value1");
map.put("key2", null);
map.put("key3", "value3");

map.entrySet().removeIf(entry -> entry.getValue() == null);