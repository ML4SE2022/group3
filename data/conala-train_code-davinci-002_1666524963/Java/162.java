import java.util.Random;

public class RandomNumberGenerator {
    public static void main(String[] args) {
        Random random = new Random();
        int[] distribution = new int[10];
        for (int i = 0; i < 1000000; i++) {
            distribution[random.nextInt(10)]++;
        }
        for (int i = 0; i < 10; i++) {
            System.out.println(i + ": " + distribution[i]);
        }
    }
}