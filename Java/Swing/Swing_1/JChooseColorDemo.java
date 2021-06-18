package Swing_1;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class JChooseColorDemo {

    public static void main(String[] args) {
        final JFrame frame = new JFrame("JColorChooser Demo");

        JButton btn1 = new JButton("Choose Color");

        btn1.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                Color newColor = JColorChooser.showDialog(
                     frame,
                     "Choose Background Color",
                     frame.getBackground());
                if(newColor != null){
                    frame.getContentPane().setBackground(newColor);
                }
            }
        });

        Container pane = frame.getContentPane();
        pane.setLayout(new FlowLayout());
        pane.add(btn1);

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 200);
        frame.setVisible(true);
    }
}
