import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[][] ndarray = {{1, 2, 3}, {4, 5, 6}};
        int[] array = Arrays.stream(ndarray).flatMapToInt(Arrays::stream).toArray();
        System.out.println(Arrays.toString(array));
    }
}