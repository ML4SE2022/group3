import java.io.BufferedReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;
import java.net.URLConnection;

public class Main {
    public static void main(String[] args) throws IOException {
        URL url = new URL("https://jsonplaceholder.typicode.com/todos/1");
        URLConnection connection = url.openConnection();
        BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()));
        String inputLine;
        StringBuilder content = new StringBuilder();
        while ((inputLine = in.readLine()) != null) {
            content.append(inputLine);
        }
        in.close();
        FileWriter fileWriter = new FileWriter("todo.json");
        fileWriter.write(content.toString());
        fileWriter.close();
    }
}