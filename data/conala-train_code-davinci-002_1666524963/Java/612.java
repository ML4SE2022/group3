import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class Main {

    public static void main(String[] args) throws IOException {
        String url = "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)";
        Document doc = Jsoup.connect(url).get();
        Elements table = doc.select("table.wikitable");
        Elements rows = table.select("tr");
        List<String> countries = new ArrayList<String>();
        List<String> populations = new ArrayList<String>();
        for (int i = 1; i < rows.size(); i++) {
            Element row = rows.get(i);
            Elements cols = row.select("td");
            countries.add(cols.get(1).text());
            populations.add(cols.get(2).text());
        }
        for (int i = 0; i < countries.size(); i++) {
            System.out.println(countries.get(i) + ": " + populations.get(i));
        }
    }
}