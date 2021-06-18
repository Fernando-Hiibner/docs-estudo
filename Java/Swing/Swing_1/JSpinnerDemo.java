package Swing_1;

import java.awt.*;
import java.util.*;
import javax.swing.*;

public class JSpinnerDemo {
    public static void main(String[] args) {
        try
        {
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        }
        catch(Exception e)
        {
            System.out.println("Falha: "+e);
        }
        JFrame frame = new JFrame("JSpinner Demo");

        // Spinner with number
        SpinnerNumberModel snm = new SpinnerNumberModel(
                new Integer(0),
                new Integer(0),
                new Integer(100),
                new Integer(5)
        );
        JSpinner spnNumber = new JSpinner(snm);

        // Spinner with Dates
        SpinnerModel snd = new SpinnerDateModel(
                new Date(),
                null,
                null,
                Calendar.DAY_OF_MONTH
        );
        JSpinner spnDate = new JSpinner(snd);

        // Spinner with List
        String[] colors = {"Red","Green","Blue"};
        SpinnerModel snl = new SpinnerListModel(colors);
        JSpinner spnList = new JSpinner(snl);

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(600, 100);

        Container cont = frame.getContentPane();

        cont.setLayout(new FlowLayout());
        cont.add(new JLabel("Select Number:"));
        cont.add(spnNumber);

        cont.add(new JLabel("Select Date:"));
        cont.add(spnDate);

        cont.add(new JLabel("Select Color:"));
        cont.add(spnList);

        frame.setVisible(true);
    }
}