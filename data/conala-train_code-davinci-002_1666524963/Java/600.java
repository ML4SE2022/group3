public static String getDayOfWeek(String dateString) {
    SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd");
    Date date = null;
    try {
        date = format.parse(dateString);
    } catch (ParseException e) {
        e.printStackTrace();
    }
    Calendar calendar = Calendar.getInstance();
    calendar.setTime(date);
    int dayOfWeek = calendar.get(Calendar.DAY_OF_WEEK);
    String dayOfWeekString = "";
    switch (dayOfWeek) {
        case 1:
            dayOfWeekString = "Sunday";
            break;
        case 2:
            dayOfWeekString = "Monday";
            break;
        case 3:
            dayOfWeekString = "Tuesday";
            break;
        case 4:
            dayOfWeekString = "Wednesday";
            break;
        case 5:
            dayOfWeekString = "Thursday";
            break;
        case 6:
            dayOfWeekString = "Friday";
            break;
        case 7:
            dayOfWeekString = "Saturday";
            break;
    }
    return dayOfWeekString;
}