public static void main(String[] args) {
    LocalDate start = LocalDate.of(2020, 1, 1);
    LocalDate end = LocalDate.of(2020, 12, 31);
    List<LocalDate> dates = new ArrayList<>();
    while (start.isBefore(end)) {
        LocalDate date = start.with(TemporalAdjusters.dayOfWeekInMonth(2, DayOfWeek.FRIDAY));
        dates.add(date);
        start = start.plusMonths(1);
    }
    System.out.println(dates);
}