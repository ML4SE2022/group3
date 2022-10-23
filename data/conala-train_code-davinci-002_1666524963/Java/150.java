public static int findMax(Map<String, Object> map) {
    int max = Integer.MIN_VALUE;
    for (Map.Entry<String, Object> entry : map.entrySet()) {
        if (entry.getValue() instanceof Integer) {
            max = Math.max(max, (Integer) entry.getValue());
        } else if (entry.getValue() instanceof Map) {
            max = Math.max(max, findMax((Map<String, Object>) entry.getValue()));
        }
    }
    return max;
}