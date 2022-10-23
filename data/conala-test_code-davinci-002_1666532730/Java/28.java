public class ListOfDictsToDictOfLists {
    public static void main(String[] args) {
        List<Map<String, String>> listOfDicts = new ArrayList<>();
        Map<String, String> dict1 = new HashMap<>();
        dict1.put("a", "1");
        dict1.put("b", "2");
        listOfDicts.add(dict1);
        Map<String, String> dict2 = new HashMap<>();
        dict2.put("a", "3");
        dict2.put("b", "4");
        listOfDicts.add(dict2);
        Map<String, String> dict3 = new HashMap<>();
        dict3.put("a", "5");
        dict3.put("b", "6");
        listOfDicts.add(dict3);

        Map<String, List<String>> dictOfLists = new HashMap<>();
        for (Map<String, String> dict : listOfDicts) {
            for (Map.Entry<String, String> entry : dict.entrySet()) {
                if (!dictOfLists.containsKey(entry.getKey())) {
                    dictOfLists.put(entry.getKey(), new ArrayList<>());
                }
                dictOfLists.get(entry.getKey()).add(entry.getValue());
            }
        }

        System.out.println(dictOfLists);
    }
}