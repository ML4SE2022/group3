import java.net.URL;
import java.net.HttpURLConnection;

public class CheckURL {
    public static void main(String[] args) {
        try {
            URL url = new URL("http://www.google.com");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.connect();

            int code = connection.getResponseCode();
            System.out.println("Response code of the object is " + code);
            if (code == 200) {
                System.out.println("OK");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}