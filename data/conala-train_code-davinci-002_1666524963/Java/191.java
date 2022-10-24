import java.util.Calendar;
import java.util.Date;
import java.util.TimeZone;

public class Main {
    public static void main(String[] args) {
        Date date = new Date();
        Calendar calendar = Calendar.getInstance();
        calendar.setTime(date);
        calendar.setTimeZone(TimeZone.getTimeZone("UTC"));
        System.out.println(calendar.getTime());
    }
}