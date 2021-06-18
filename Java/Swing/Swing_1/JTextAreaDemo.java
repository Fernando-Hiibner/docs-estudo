package Swing_1;

import javax.swing.*;
import java.awt.*;

public class JTextAreaDemo {

    public static void main(String[] args) {
        try
        {
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        }
        catch(Exception e)
        {
            System.out.println("Falha: "+e);
        }
        final JFrame frame = new JFrame("JTextArea Demo");
        JTextArea ta = new JTextArea(10, 20);

        JScrollPane sp = new JScrollPane(ta);

        frame.setLayout(new FlowLayout());
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 220);
        frame.getContentPane().add(sp);

        frame.setVisible(true);
    }
}
