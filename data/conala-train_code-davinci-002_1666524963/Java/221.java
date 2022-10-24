public class Main {
    public static void main(String[] args) {
        Map<String, String> map1 = new HashMap<>();
        map1.put("key1", "value1");
        map1.put("key2", "value2");
        map1.put("key3", "value3");

        Map<String, String> map2 = new HashMap<>();
        map2.put("key3", "value3");
        map2.put("key2", "value2");
        map2.put("key1", "value1");

        System.out.println(map1.hashCode());
        System.out.println(map2.hashCode());
    }
}