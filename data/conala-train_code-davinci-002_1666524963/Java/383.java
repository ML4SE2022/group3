LocalDate today = LocalDate.now();
LocalDate other = LocalDate.of(2012, Month.MARCH, 12);
if (today.equals(other)) {
    System.out.println("Today and date are the same day!");
}