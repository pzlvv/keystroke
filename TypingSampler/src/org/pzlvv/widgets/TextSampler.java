package org.pzlvv.widgets;

import javax.swing.*;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.awt.event.WindowEvent;
import java.io.*;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.security.Timestamp;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

public class TextSampler extends JTextField {
    public TextSampler(String target) {
        new File("data").mkdir();
        this.target = target;
        remain = target;
        this.addKeyListener(new KeyListener() {
            @Override
            public void keyTyped(KeyEvent e) {
                if (remain.length() > 0) {
                    if (remain.charAt(0) != e.getKeyChar()) {
                        e.consume();
                        retype();
                    } else {
                        remain = remain.substring(1);
                    }
                }
            }

            @Override
            public void keyPressed(KeyEvent e) {
                if (remain.length() == 0 && e.getKeyCode() != KeyEvent.VK_ENTER) {
                    e.consume();
                    retype();
                } else {
                    String item = "%d %d 0";
                    long curTime = System.currentTimeMillis();
                    records.add(String.format(item, curTime, e.getKeyCode()));
                    System.out.println(e.getKeyChar()+" 0");
                }
            }

            @Override
            public void keyReleased(KeyEvent e) {
                String item = "%d %d 1";
                long curTime = System.currentTimeMillis();
                records.add(String.format(item, curTime, e.getKeyCode()));
                System.out.println(e.getKeyChar()+" 1");
                if (remain.length() == 0 && e.getKeyCode() == KeyEvent.VK_ENTER) {
                    submit();
                }
            }

        });
    }

    private void retype() {
        this.setText("");
        remain = target;
        records.clear();
        JOptionPane.showMessageDialog(null, "Sample failed due to wrong input, clear to retype.");
    }

    private void submit() {
        File file = new File(Paths.get("data", sampleTimes + ".log").toString());
        try {
            PrintStream ps = new PrintStream(file);
            for (String record : records) {
                ps.println(record);
            }
            ps.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        --sampleTimes;
        if (0 < sampleTimes) {
            JOptionPane.showMessageDialog(null, "Sample success, left sample times: " + sampleTimes);
            this.setText("");
            remain = target;
            records.clear();
        } else {
            JOptionPane.showMessageDialog(null, "Thanks for cooperation, package and send the data directory to pz.pzlvv@gmail.com." );
            System.exit(0);
        }
    }

    private String remain;
    private String target;
    private int sampleTimes = 20;
    private List<String> records = new ArrayList<>();

}
