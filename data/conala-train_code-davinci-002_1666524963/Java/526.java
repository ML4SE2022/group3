public class TimeOffset {
    public static void main(String[] args) {
        LocalDateTime now = LocalDateTime.now();
        System.out.println(now);
        LocalDateTime nowPlus = now.plusHours(2);
        System.out.println(nowPlus);
        System.out.println(nowPlus.getHour());
        System.out.println(nowPlus.getMinute());
        System.out.println(nowPlus.getSecond());
        System.out.println(nowPlus.getNano());
        System.out.println(nowPlus.getDayOfMonth());
        System.out.println(nowPlus.getDayOfYear());
        System.out.println(nowPlus.getDayOfWeek());
        System.out.println(nowPlus.getMonth());
        System.out.println(nowPlus.getMonthValue());
        System.out.println(nowPlus.getYear());
        System.out.println(nowPlus.getChronology());
        System.out.println(nowPlus.getEra());
        System.out.println(nowPlus.getOffset());
        System.out.println(nowPlus.get(ChronoField.HOUR_OF_DAY));
        System.out.println(nowPlus.get(ChronoField.MINUTE_OF_HOUR));
        System.out.println(nowPlus.get(ChronoField.SECOND_OF_MINUTE));
        System.out.println(nowPlus.get(ChronoField.NANO_OF_SECOND));
        System.out.println(nowPlus.get(ChronoField.DAY_OF_MONTH));
        System.out.println(nowPlus.get(ChronoField.DAY_OF_YEAR));
        System.out.println(nowPlus.get(ChronoField.DAY_OF_WEEK));
        System.out.println(nowPlus.get(ChronoField.MONTH_OF_YEAR));
        System.out.println(nowPlus.get(ChronoField.YEAR));
        System.out.println(