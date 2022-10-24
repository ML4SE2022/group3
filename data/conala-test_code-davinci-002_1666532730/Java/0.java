public static <K, V> Map<K, List<V>> transpose(List<Map<K, V>> list) {
    Map<K, List<V>> result = new HashMap<>();
    for (Map<K, V> map : list) {
        for (Map.Entry<K, V> entry : map.entrySet()) {
            List<V> values = result.get(entry.getKey());
            if (values == null) {
                values = new ArrayList<>();
                result.put(entry.getKey(), values);
            }
            values.add(entry.getValue());
        }
    }
    return result;
}