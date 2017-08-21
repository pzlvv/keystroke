package org.pzlvv.widgets;

import javax.swing.*;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class TextSampler extends JTextField {
    public TextSampler(String target) {
        this.target = target;
        remain = target;
        this.addKeyListener(new KeyListener() {
            @Override
            public void keyTyped(KeyEvent e) {
                if (remain.length() > 0 ) {
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
                }
            }

            @Override
            public void keyReleased(KeyEvent e) {
                if (remain.length() == 0 && e.getKeyCode() == KeyEvent.VK_ENTER) {
                    System.out.println("submit");
                }
            }

        });
    }
    private void retype() {
        this.setText("");
        remain = target;
    }
    private String remain;
    private String target;

}
