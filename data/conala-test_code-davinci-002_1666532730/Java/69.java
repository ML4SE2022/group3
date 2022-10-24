String cp1251 = "Привет";
String utf8 = new String(cp1251.getBytes("CP1251"), "UTF-8");