public static void main(String[] args) {
    int[] arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int random = (int) (Math.random() * arr.length);
    System.out.println(arr[random]);
}