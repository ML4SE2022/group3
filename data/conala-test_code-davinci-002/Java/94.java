public static void main(String[] args) {
    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
    LocalDateTime dateTime = LocalDateTime.parse("2019-01-01 00:00:00", formatter);
    System.out.println(dateTime.plusYears(100));
}