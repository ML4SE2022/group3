import java.util.ArrayList;
import java.util.List;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

public class Main {

    public static void main(String[] args) {
        Gson gson = new GsonBuilder().create();
        List<String> list = new ArrayList<>();
        list.add("a");
        list.add("b");
        list.add("c");
        String json = gson.toJson(list);
        System.out.println(json);
    }
}