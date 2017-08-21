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
        JLabel prompt = new JLabel("Where is the bug");
        JTextField tf = new TextSampler("Where is the bug");
        tf.setColumns(10);
        tf.setFont(font);

        Panel panel = new Panel();
        panel.add(tf);
        contentPane.add(prompt);
        //contentPane.add(tf);
        contentPane.add(panel);

        this.setSize(400, 300);
        Dimension dim = Toolkit.getDefaultToolkit().getScreenSize();
        this.setLocation(dim.width/2-this.getSize().width/2, dim.height/2-this.getSize().height/2);
        this.setVisible(true);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
