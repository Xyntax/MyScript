/**
 * 
 */
package com.xuyueg.client;

import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.awt.HeadlessException;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.text.SimpleDateFormat;
import java.util.Date;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import com.xuyue.client.ClientMainWindow;
import com.xuyue.client.SendThread;

/**
 * @author xuyue
 *
 */
public class ClientMainWindow extends JFrame implements ActionListener {

	/**
	 * 
	 */
	private static final long serialVersionUID = -7488994958453903490L;
	private JTextArea textArea;
	private JButton startButton;
	private JButton stopButton;

	SendThread st;
	
	public ClientMainWindow() throws HeadlessException {
		
		initUI();
		this.appendMessage("发送端已启动！");
	}

	private void initUI(){
		this.setLayout(new BorderLayout());
		textArea = new JTextArea();
		textArea.setEditable(false);
		startButton = new JButton("开始");
		stopButton = new JButton("停止");
		JPanel south = new JPanel();
		south.setLayout(new GridLayout(2, 3, 5, 5));
		south.add(startButton);
		south.add(stopButton);
		startButton.addActionListener(this);
		stopButton.addActionListener(this);
		this.add(new JScrollPane(textArea), "Center");
		this.add(south, "South");
		this.setSize(640, 480);
		this.setTitle("MyGBN-Client");
		this.setLocationRelativeTo(null);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setVisible(true);
	}
	
	
	public void appendMessage(String message){
		SimpleDateFormat sdf = new SimpleDateFormat("YYYY-MM-dd HH:mm:ss.SSS");
		textArea.append(sdf.format(new Date()) + " " + message + "\n");
		textArea.setCaretPosition(textArea.getDocument().getLength());
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		if(e.getSource() == startButton){
			st = new SendThread(this);
			st.start();
		}else if(e.getSource() == stopButton){
			if(st != null){
				st.forceStop();
			}
		}
	}
	
	public static void main(String []args){
		new ClientMainWindow();
	}

}
