package Swing_1;

import java.awt.BorderLayout;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
import javax.swing.JCheckBox;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;

public class CheckBoxDemo {

    public static void main(String[] args) {
        final JFrame frame = new JFrame("JCheckBox Demo");

        JCheckBox chkSwing = new JCheckBox("Java Swing");
        chkSwing.addItemListener(
                new ItemListener() {
                    public void itemStateChanged(ItemEvent e) {
                        if (e.getStateChange() == ItemEvent.SELECTED) {
                            JOptionPane.showMessageDialog(frame,
                                    "CheckBox is selected");
                        } else {
                            JOptionPane.showMessageDialog(frame,
                                    "CheckBox is unselected");
                        }
                    }
                });
        // Add checkbox to a panel
        JPanel buttonPanel = new JPanel();
        buttonPanel.add(chkSwing);
        // Frame setting
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 100);
        frame.getContentPane().add(buttonPanel, BorderLayout.SOUTH);
        frame.setVisible(true);
    }
}
