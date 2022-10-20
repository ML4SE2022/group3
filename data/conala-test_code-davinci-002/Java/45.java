import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.URL;

public class DownloadFile {
    public static void main(String[] args) throws IOException {
        String url = "http://www.example.com/example.zip";
        String file = "example.zip";
        downloadUsingStream(url, file);
    }

    private static void downloadUsingStream(String urlStr, String file) throws IOException{
        URL url = new URL(urlStr);
        InputStream is = url.openStream();
        FileOutputStream fos = new FileOutputStream(file);

        byte[] buffer = new byte[4096];
        int bytesRead = 0;

        System.out.print("Downloading " + urlStr + " ... ");
        while ((bytesRead = is.read(buffer)) != -1) {
            fos.write(buffer, 0, bytesRead);
        }
        System.out.println("done!");

        fos.close();
        is.close();
    }
}