import java.util.Date;
import java.text.DateFormat;
import java.text.SimpleDateFormat;

DateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
Date date = new Date();
System.out.println(dateFormat.format(date)); //2016/11/16 12:08:43