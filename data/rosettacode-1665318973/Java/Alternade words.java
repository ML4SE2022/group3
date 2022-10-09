import java.io.*;
import java.util.*;

public class AlternadeWords {
    public static void main(String[] args) {
        try {
            Set<String> dictionary = new TreeSet<>();
            try (BufferedReader reader = new BufferedReader(new FileReader("unixdict.txt"))) {
                String line;
                while ((line = reader.readLine()) != null)
                    dictionary.add(line);
            }
            StringBuilder word1 = new StringBuilder();
            StringBuilder word2 = new StringBuilder();
            for (String word : dictionary) {
                int length = word.length();
                if (length < 6)
                    continue;
                word1.setLength(0);
                word2.setLength(0);
                for (int i = 0; i < length; i += 2) {
                    word1.append(word.charAt(i));
                    if (i + 1 < length)
                        word2.append(word.charAt(i + 1));
                }
                String w1 = word1.toString();
                String w2 = word2.toString();
                if (dictionary.contains(w1) && dictionary.contains(w2))
                    System.out.printf("%-10s%-6s%s\n", word, w1, w2);
            }
        } catch (Exception e)  {
            e.printStackTrace();
        }
    }
}