import java.io.FileReader;
import java.io.IOException;
import java.nio.charset.StandardCharsets;

public class Main {

    public static void main(String[] args) throws IOException {
        var reader = new FileReader("input.txt", StandardCharsets.UTF_8);
        while (true) {
            int c = reader.read();
            if (c == -1) break;
            System.out.print(Character.toChars(c));
        }
    }
}