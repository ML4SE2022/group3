public class SortJson {
    public static void main(String[] args) throws IOException {
        String json = "{\"a\":1,\"b\":2,\"c\":3,\"d\":4,\"e\":5}";
        ObjectMapper mapper = new ObjectMapper();
        Map<String, Integer> map = mapper.readValue(json, new TypeReference<Map<String, Integer>>() {
        });
        Map<String, Integer> sortedMap = map.entrySet().stream()
                .sorted(Map.Entry.comparingByKey())
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue,
                        (oldValue, newValue) -> oldValue, LinkedHashMap::new));
        System.out.println(sortedMap);
    }
}