public static <K, V extends Comparable<? super V>> K maxKey(Map<K, V> map) {
    Entry<K, V> max = null;
    for (Entry<K, V> entry : map.entrySet()) {
        if (max == null || entry.getValue().compareTo(max.getValue()) > 0) {
            max = entry;
        }
    }
    return max.getKey();
}