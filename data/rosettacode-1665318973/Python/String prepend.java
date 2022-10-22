// prepend
public class Prepend {
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder("world");
        sb.insert(0, "Hello, ");
        System.out.println(sb);
    }
}