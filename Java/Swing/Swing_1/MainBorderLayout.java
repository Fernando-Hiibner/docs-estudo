package Swing_1;
import javax.swing.*;
import java.awt.*;


public class MainBorderLayout extends JFrame
{
    private Container c;
    public MainBorderLayout()
    {
        try
        {
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        }
        catch(Exception e)
        {
            System.out.println("Erro ao mudar lookAndFeel: "+e);
        }
        c = getContentPane();
        setSize(300, 400);
        setTitle("Estudando Swing 1");
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        this.firstScreen();
    }
    public void firstScreen()
    {
        JPanel mainPannel = new JPanel(new BorderLayout());

        JButton pageSButton  = new JButton("PAGE_START");
        JButton lineSButton  = new JButton("LINE_START");
        JButton centerButton = new JButton("CENTER");
        JButton lineEButton  = new JButton("LINE_END");
        JButton pageEButton  = new JButton("PAGE_END");

        mainPannel.add(pageSButton, BorderLayout.PAGE_START);
        mainPannel.add(lineSButton, BorderLayout.LINE_START);
        mainPannel.add(centerButton, BorderLayout.CENTER);
        mainPannel.add(lineEButton, BorderLayout.LINE_END);
        mainPannel.add(pageEButton, BorderLayout.PAGE_END);

        c.add(mainPannel);
    }
    public static void main(String args[])
    {
        MainBorderLayout demo = new MainBorderLayout();
        demo.setVisible(true);
    }
}