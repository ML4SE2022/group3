import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.Ellipse2D;
import java.awt.geom.Line2D;
import javax.swing.JComponent;

public class PlotComponent extends JComponent {
    public void paintComponent(Graphics g) {
        Graphics2D g2 = (Graphics2D) g;
        Ellipse2D.Double circle = new Ellipse2D.Double(0, 0, 20, 20);
        g2.draw(circle);
        Line2D.Double line = new Line2D.Double(0, 0, 20, 20);
        g2.draw(line);
    }
}
```

```java
import javax.swing.JFrame;

public class PlotFrame extends JFrame {
    public PlotFrame() {
        setSize(300, 400);
        setTitle("Plot Frame");
        PlotComponent component = new PlotComponent();
        add(component);
    }
}
```

```java
import javax.swing.JFrame;

public class PlotViewer {
    public static void main(String[] args) {
        JFrame frame = new PlotFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}