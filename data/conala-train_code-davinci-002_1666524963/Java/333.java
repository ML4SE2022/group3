import java.util.Random;

public class RandomColor {
    public static void main(String[] args) {
        Random random = new Random();
        int r = random.nextInt(256);
        int g = random.nextInt(256);
        int b = random.nextInt(256);
        System.out.println("r = " + r);
        System.out.println("g = " + g);
        System.out.println("b = " + b);
    }
}