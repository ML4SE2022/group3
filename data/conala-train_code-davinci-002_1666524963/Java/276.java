String html = "<div id='foo'>foo</div><div id='bar'>bar</div><div id='baz'>baz</div>";
Document doc = Jsoup.parse(html);
Elements elements = doc.select("div[id$=az]");