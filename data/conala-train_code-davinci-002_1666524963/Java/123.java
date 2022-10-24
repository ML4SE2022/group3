public static void main(String[] args) {
    String html = "<html><body><div><p>Hello</p><p>World</p></div></body></html>";
    Document doc = Jsoup.parse(html);
    Element p = doc.select("p:contains(World)").first();
    System.out.println(p.text());
}