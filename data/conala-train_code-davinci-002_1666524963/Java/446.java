public static List<Map<String, Object>> split(Map<String, List<Object>> map) {
    List<Map<String, Object>> result = new ArrayList<>();
    for (Map.Entry<String, List<Object>> entry : map.entrySet()) {
        for (Object value : entry.getValue()) {
            Map<String, Object> item = new HashMap<>();
            item.put(entry.getKey(), value);
            result.add(item);
        }
    }
    return result;
}