import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;

public class Replace {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner console = new Scanner(System.in);
        System.out.print("Input file: ");
        String inputFileName = console.next();
        System.out.print("Output file: ");
        String outputFileName = console.next();
        System.out.print("Old: ");
        String old = console.next();
        System.out.print("New: ");
        String replacement = console.next();

        File inputFile = new File(inputFileName);
        Scanner in = new Scanner(inputFile);
        PrintWriter out = new PrintWriter(outputFileName);
        while (in.hasNextLine()) {
            String line = in.nextLine();
            line = line.replace(old, replacement);
            out.println(line);
        }
        in.close();
        out.close();
    }
}