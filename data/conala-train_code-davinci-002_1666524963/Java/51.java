import java.awt.Font;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.awt.geom.AffineTransform;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class Main extends JPanel {

    private void doDrawing(Graphics g) {

        Graphics2D g2d = (Graphics2D) g;

        g2d.setColor(Color.blue);

        RenderingHints rh = new RenderingHints(
                RenderingHints.KEY_ANTIALIASING,
                RenderingHints.VALUE_ANTIALIAS_ON);

        rh.put(RenderingHints.KEY_RENDERING,
               RenderingHints.VALUE_RENDER_QUALITY);

        g2d.setRenderingHints(rh);

        Font font = new Font("Serif", Font.PLAIN, 24);
        g2d.setFont(font);

        g2d.drawString("Java 2D", 50, 50);

        AffineTransform at = new AffineTransform();
        at.rotate(Math.PI/4);

        Font f = font.deriveFont(at);
        g2d.setFont(f);

        g2d.drawString("Java 2D", 50, 150);
    }

    @Override
    public void paintComponent(Graphics g) {

        super.paintComponent(g);
        doDrawing(g);
    }

    public static void main(String[] args) {

        JFrame frame = new JFrame("Java 2D");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(new Main());
        frame.setSize(350, 250);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }
}