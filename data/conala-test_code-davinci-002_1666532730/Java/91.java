public static void main(String[] args) {
    LocalDateTime now = LocalDateTime.now();
    LocalDateTime plus = now.plusYears(100);
    LocalDateTime minus = now.minusYears(100);
    System.out.println(now);
    System.out.println(plus);
    System.out.println(minus);
}