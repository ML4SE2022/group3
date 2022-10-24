String text = "";
Elements elements = doc.select("div.class");
for (Element element : elements) {
    text = element.text();
}