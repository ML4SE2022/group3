List<Map<String, Object>> list = new ArrayList<>();
Map<String, Object> map = new HashMap<>();
map.put("name", "John");
map.put("age", 30);
list.add(map);

String name = (String) list.get(0).get("name");
Integer age = (Integer) list.get(0).get("age");