import java.io.File;
import java.text.SimpleDateFormat;

public class FileDate {
    public static void main(String[] args) {
        File file = new File("/tmp/foo.txt");
        SimpleDateFormat sdf = new SimpleDateFormat("MM/dd/yyyy HH:mm:ss");

        System.out.println("Last Modified Date: " + sdf.format(file.lastModified()));
        System.out.println("Created Date: " + sdf.format(file.lastModified()));
    }
}