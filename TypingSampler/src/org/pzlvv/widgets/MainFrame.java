package org.pzlvv.widgets;

import javax.swing.*;
import java.awt.*;

public class MainFrame extends JFrame{
    public MainFrame() {
        super("Typing Sampler");
        JLabel label=new JLabel("Hello world!");
        JPanel contentPane=new JPanel();
        this.setContentPane(contentPane);
        contentPane.setLayout(new BoxLayout(contentPane, BoxLayout.Y_AXIS));

        Font font = new Font("SansSerif", Font.BOLD, 20);
        JLabel prompt1 = new JLabel("Type the following sentence ended with ENTER key");
        JLabel prompt2 = new JLabel("          Where is the fox");
        JTextField tf = new TextSampler("Where is the fox");
        tf.setColumns(10);
        tf.setFont(font);

        prompt2.setFont(font);

        Panel panel = new Panel();
        panel.add(tf);
        contentPane.add(prompt1);
        contentPane.add(prompt2);
        //contentPane.add(tf);
        contentPane.add(panel);

        this.setSize(400, 300);
        Dimension dim = Toolkit.getDefaultToolkit().getScreenSize();
        this.setLocation(dim.width/2-this.getSize().width/2, dim.height/2-this.getSize().height/2);
        this.setVisible(true);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
