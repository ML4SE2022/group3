import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class ReadFiles {
    public static void main(String[] args) {
        File file = new File("/Users/joe/Desktop/test");
        readFiles(file);
    }

    public static void readFiles(File file) {
        if (file.isDirectory()) {
            File[] files = file.listFiles();
            for (File f : files) {
                readFiles(f);
            }
        } else {
            try {
                Scanner scanner = new Scanner(file);
                while (scanner.hasNext()) {
                    System.out.println(scanner.nextLine());
                }
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
        }
    }
}