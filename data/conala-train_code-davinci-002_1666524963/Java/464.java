import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;

public class RemoveWhiteSpace {
    public static void main(String[] args) throws IOException {
        BufferedImage image = ImageIO.read(new File("image.png"));
        int width = image.getWidth();
        int height = image.getHeight();
        int minX = width;
        int minY = height;
        int maxX = -1;
        int maxY = -1;
        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                int  pixel = image.getRGB(x, y);
                if (pixel != Color.WHITE.getRGB()) {
                    if (minX > x) minX = x;
                    if (maxX < x) maxX = x;
                    if (minY > y) minY = y;
                    if (maxY < y) maxY = y;
                }
            }
        }
        BufferedImage result = new BufferedImage(maxX - minX + 1, maxY - minY + 1, BufferedImage.TYPE_INT_ARGB);
        Graphics2D g = result.createGraphics();
        g.drawImage(image, 0, 0, result.getWidth(), result.getHeight(), minX, minY, maxX + 1, maxY + 1, null);
        g.dispose();
        ImageIO.write(result, "png", new File("result.png"));
    }
}