public static List<Map<String, Object>> sort(List<Map<String, Object>> list, String order) {
    List<Map<String, Object>> sortedList = new ArrayList<>();
    for (String key : order.split(",")) {
        for (Map<String, Object> map : list) {
            if (map.get("key").equals(key)) {
                sortedList.add(map);
            }
        }
    }
    return sortedList;
}