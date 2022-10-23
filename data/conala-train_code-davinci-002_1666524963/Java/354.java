public class Binary4Tuple {
    public static void main(String[] args) {
        for (int i = 0; i < 16; i++) {
            System.out.println(String.format("%4s", Integer.toBinaryString(i)).replace(' ', '0'));
        }
    }
}