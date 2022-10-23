import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class WriteToFile {
    public static void main(String[] args) {
        String[][] data = new String[3][2];
        data[0][0] = "1";
        data[0][1] = "2";
        data[1][0] = "3";
        data[1][1] = "4";
        data[2][0] = "5";
        data[2][1] = "6";

        try {
            File file = new File("C:\\Users\\User\\Desktop\\test.txt");
            FileWriter writer = new FileWriter(file);
            for (int i = 0; i < data.length; i++) {
                for (int j = 0; j < data[i].length; j++) {
                    writer.write(data[i][j] + " ");
                }
                writer.write("\r\n");
            }
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}