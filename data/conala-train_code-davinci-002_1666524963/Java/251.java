String html = "<html><head><title>Test</title></head><body>\u00A0</body></html>";
Document doc = Jsoup.parse(html);
String text = doc.text();
System.out.println(text);