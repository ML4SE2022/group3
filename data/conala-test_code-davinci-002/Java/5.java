import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class Main {

    public static void main(String[] args) {
        String html = "<html><head><title>Sample Title</title></head>"
                + "<body>"
                + "<div id='sampleDiv'><a id='googleA' href='www.google.com'>Google</a></div>"
                + "<div id='sampleDiv' class='bold'><a id='yahooA' href='www.yahoo.com'>Yahoo</a></div>"
                + "<div id='sampleDiv' class='bold'><a id='msnA' href='www.msn.com'>MSN</a></div>"
                + "</body></html>";

        Document doc = Jsoup.parse(html);

        Elements elements = doc.select("div.bold");
        for (Element element : elements) {
            element.remove();
        }

        System.out.println(doc);
    }
}