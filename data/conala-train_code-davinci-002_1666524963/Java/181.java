String s = "ÄÖÜäöüß";
byte[] bytes = s.getBytes("ISO-8859-1");
String s2 = new String(bytes, "UTF-8");