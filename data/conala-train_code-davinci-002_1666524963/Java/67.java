public static Map<String, String> merge(List<Map<String, String>> maps) {
    Map<String, String> result = new HashMap<>();
    for (Map<String, String> map : maps) {
        result.putAll(map);
    }
    return result;
}