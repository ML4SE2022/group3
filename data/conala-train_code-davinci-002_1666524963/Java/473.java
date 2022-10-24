public static int countElements(Map<String, Object> map) {
    int count = 0;
    for (Map.Entry<String, Object> entry : map.entrySet()) {
        if (entry.getValue() instanceof Map) {
            count += countElements((Map<String, Object>) entry.getValue());
        } else if (entry.getValue() instanceof List) {
            for (Object o : (List<Object>) entry.getValue()) {
                if (o instanceof Map) {
                    count += countElements((Map<String, Object>) o);
                } else {
                    count++;
                }
            }
        } else {
            count++;
        }
    }
    return count;
}