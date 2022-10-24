public static Map<String, String> toMap(List<List<String>> list) {
    Map<String, String> map = new HashMap<>();
    for (List<String> entry : list) {
        map.put(entry.get(0), entry.get(1));
    }
    return map;
}