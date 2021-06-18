package Swing_1;

import java.awt.*;
import javax.swing.*;
import javax.swing.event.*;

public class JSpinnerEventDemo {
    public static void main(String[] args) {
        final JFrame frame = new JFrame("JSpinner Demo");

        // Spinner with number
        SpinnerNumberModel snm = new SpinnerNumberModel(
                new Integer(0),
                new Integer(0),
                new Integer(100),
                new Integer(5)
        );
        final JSpinner spnNumber = new JSpinner(snm);
        // Add change listener to the spinner
        spnNumber.addChangeListener(
                new ChangeListener(){
                   public void stateChanged(ChangeEvent e) {
                         JOptionPane.showMessageDialog(frame,
                                "\nCurrent value:" +
                                spnNumber.getModel().getValue() +
                                "\nPrevious value:" +
                                spnNumber.getModel().getPreviousValue() +
                                "\nNext value:" +
                                spnNumber.getModel().getNextValue()
                                );

                   }
                }
        );

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 100);
        Container cont = frame.getContentPane();
        cont.setLayout(new FlowLayout());
        cont.add(new JLabel("Select Number:"));
        cont.add(spnNumber);
        frame.setVisible(true);
    }
}
