package Swing_1;

import javax.swing.JLabel;
import javax.swing.JFrame;

public class JLabelHTMLDemo {
    public static void main(String[] args) {

        String html = 
        "<html><span style=\"color:#ff0000;font-style:italic\">"
      + "HTML text with red color, italic font</span><</html>";
        JLabel label = new JLabel(html);

        JFrame frame = new JFrame("JLabel with HTML text");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300,200);
        frame.getContentPane().add(label);
        frame.setVisible(true);
    }
}
