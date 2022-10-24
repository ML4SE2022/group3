import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.awt.geom.Ellipse2D;
import java.awt.geom.Line2D;
import java.awt.geom.Rectangle2D;
import java.util.ArrayList;
import java.util.List;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class Plot extends JPanel {

    private static final long serialVersionUID = 1L;
    private static final int MAX_SCORE = 20;
    private static final int PREF_W = 800;
    private static final int PREF_H = 650;
    private static final int BORDER_GAP = 30;
    private static final Color GRAPH_COLOR = Color.green;
    private static final Color GRAPH_POINT_COLOR = new Color(150, 50, 50, 180);
    private static final Stroke GRAPH_STROKE = new BasicStroke(3f);
    private static final int GRAPH_POINT_WIDTH = 12;
    private static final int Y_HATCH_CNT = 10;
    private List<Integer> scores;

    public Plot(List<Integer> scores) {
        this.scores = scores;
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2 = (Graphics2D) g;
        g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

        double xScale = ((double) getWidth() - 2 * BORDER_GAP) / (scores.size() - 1);
        double yScale = ((double) getHeight() - 2 * BORDER_GAP) / (MAX_SCORE - 1);