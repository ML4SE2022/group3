public static void main(String[] args) {
    String[] numbers = "1.2.3.4.5.6.7.8.9.10".split("\\.");
    Arrays.sort(numbers, new Comparator<String>() {
        @Override
        public int compare(String o1, String o2) {
            return Integer.valueOf(o1).compareTo(Integer.valueOf(o2));
        }
    });
    System.out.println(Arrays.toString(numbers));
}