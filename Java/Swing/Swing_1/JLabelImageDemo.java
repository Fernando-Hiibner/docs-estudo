package Swing_1;

import javax.swing.ImageIcon;
import javax.swing.JLabel;
import javax.swing.JFrame;

public class JLabelImageDemo {
    public static void main(String[] args) {

        ImageIcon icon = new ImageIcon("./images/java.gif");
        JLabel label = new JLabel(icon);

        JFrame frame = new JFrame("JLabel with Image Demo");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(640,480);
        frame.getContentPane().add(label);
        frame.setVisible(true);
    }
}
