import java.util.*;

class MergeMaps {
    public static void main(String[] args) {
        Map<String, Object> base = new HashMap<>();
        base.put("name", "Rocket Skates");
        base.put("price", 12.75);
        base.put("color", "yellow");
        Map<String, Object> update = new HashMap<>();
        update.put("price", 15.25);
        update.put("color", "red");
        update.put("year", 1974);

        Map<String, Object> result = new HashMap<>(base);
        result.putAll(update);

        System.out.println(result);
    }
}