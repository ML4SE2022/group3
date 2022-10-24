String dateString = "2018-01-01";
SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
Date date = sdf.parse(dateString);
sdf = new SimpleDateFormat("yyyyMMdd");
String newDateString = sdf.format(date);