import java.util.Random;
import java.util.Set;
import java.util.TreeSet;

public class RandomNumberGenerator {

    public static void main(String[] args) {
        Random random = new Random();
        Set<Integer> set = new TreeSet<>();
        while (set.size() < 10) {
            set.add(random.nextInt(100));
        }
        System.out.println(set);
    }
}