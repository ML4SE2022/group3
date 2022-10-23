List<Map<String, Object>> list = new ArrayList<>();
list.add(new HashMap<String, Object>() {{
    put("key1", "value1");
    put("key2", "value2");
}});
list.add(new HashMap<String, Object>() {{
    put("key1", "value1");
    put("key2", "value2");
}});
list.add(new HashMap<String, Object>() {{
    put("key1", "value1");
    put("key2", "value2");
}});

list.forEach(map -> map.remove("key1"));