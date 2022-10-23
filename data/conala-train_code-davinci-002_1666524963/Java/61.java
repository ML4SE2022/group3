import java.awt.Dimension;
import java.awt.Toolkit;

import javax.swing.JFrame;

public class Main {
    public static void main(String[] args) {
        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(new Dimension(300, 300));
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }
}