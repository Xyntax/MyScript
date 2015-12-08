/**
 * 
 */
package com.xuyue.server;

import java.awt.BorderLayout;
import java.awt.HeadlessException;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.text.SimpleDateFormat;
import java.util.Date;
import javax.swing.JFrame;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import com.xuyue.common.C;
import com.xuyue.server.ReceiveThread;
import com.xuyue.server.ServerMainWindow;

/**
 * @author xuyue
 * 
 */
public class ServerMainWindow extends JFrame implements Runnable {
	/**
	 * 
	 */
	private static final long serialVersionUID = 4722150879064644474L;

	private JTextArea textArea;

	private ServerSocket serverSocket;

	private int nextExceptSequence;

	public int getNextExceptSequence() {
		return nextExceptSequence;
	}

	public void setNextExceptSequence(int nextExceptSequence) {
		this.nextExceptSequence = nextExceptSequence;
	}

	public ServerMainWindow() throws HeadlessException {

		this.setLayout(new BorderLayout());
		textArea = new JTextArea();
		textArea.setEditable(false);
		this.add(new JScrollPane(textArea), "Center");
		this.setSize(640, 480);
		this.setTitle("MyGBN-Server");
		this.setLocationRelativeTo(null);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setVisible(true);
		this.appendMessage("服务器启动成功！");

		try {
			serverSocket = new ServerSocket(C.server.port);
		} catch (IOException e) {
			this.appendMessage("网络连接失败，请重启！");
		}
		new Thread(this).start();
	}

	/*
	 * (non-Javadoc)
	 * 
	 * @see java.lang.Runnable#run()
	 */
	@Override
	public void run() {
		// TODO Auto-generated method stub
		this.appendMessage("开始等待连接！");
		this.appendMessage("开始等待packet" + nextExceptSequence);
		Socket socket = null;
		while (true) {
			try {
				socket = serverSocket.accept();
				new ReceiveThread(socket, this).start();
			} catch (IOException e) {
				e.printStackTrace();
				if (e.getMessage().equals("Connection reset")) {
					break;
				}
			}
		}
	}

	public void appendMessage(String message) {
		SimpleDateFormat sdf = new SimpleDateFormat("YYYY-MM-dd HH:mm:ss.SSS");
		textArea.append(sdf.format(new Date()) + " " + message + "\n");
		textArea.setCaretPosition(textArea.getDocument().getLength());
	}

	public static void main(String[] args) {
		new ServerMainWindow();
	}

}
