import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class Main {

    public static void main(String[] args) {
        String html = "<html><head><title>Sample Title</title></head>"
                + "<body>"
                + "<div id='sampleDiv'><a id='googleA' href='www.google.com'>Google</a></div>"
                + "<div id='sampleDiv'><a id='yahooA' href='www.yahoo.com'>Yahoo</a></div>"
                + "</body></html>";

        Document doc = Jsoup.parse(html);

        Elements divs = doc.select("div");
        for (Element div : divs) {
            if (div.attr("id").equals("sampleDiv")) {
                div.remove();
            }
        }

        System.out.println(doc.toString());
    }
}