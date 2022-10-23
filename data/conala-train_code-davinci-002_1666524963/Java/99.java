import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class DosLineBreaks {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader("file.txt"));
        String line;
        while ((line = reader.readLine()) != null) {
            if (line.endsWith("\r")) {
                System.out.println("DOS line break detected");
            }
        }
    }
}