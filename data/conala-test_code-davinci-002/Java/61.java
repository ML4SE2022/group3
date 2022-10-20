public class ListOfDictsToDictOfLists {
    public static void main(String[] args) {
        List<Map<String, Object>> listOfDicts = new ArrayList<>();
        Map<String, Object> dict1 = new HashMap<>();
        dict1.put("name", "John");
        dict1.put("age", 30);
        listOfDicts.add(dict1);
        Map<String, Object> dict2 = new HashMap<>();
        dict2.put("name", "Mary");
        dict2.put("age", 25);
        listOfDicts.add(dict2);
        Map<String, Object> dict3 = new HashMap<>();
        dict3.put("name", "Bob");
        dict3.put("age", 35);
        listOfDicts.add(dict3);

        Map<String, List<Object>> dictOfLists = new HashMap<>();
        for (Map<String, Object> dict : listOfDicts) {
            for (Map.Entry<String, Object> entry : dict.entrySet()) {
                String key = entry.getKey();
                Object value = entry.getValue();
                if (!dictOfLists.containsKey(key)) {
                    dictOfLists.put(key, new ArrayList<>());
                }
                dictOfLists.get(key).add(value);
            }
        }

        System.out.println(dictOfLists);
    }
}