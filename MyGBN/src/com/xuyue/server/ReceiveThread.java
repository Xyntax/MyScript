/**
 * 
 */
package com.xuyue.server;

import java.io.EOFException;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;
import java.net.SocketException;

import com.xuyue.common.C;
import com.xuyue.common.Packet;
import com.xuyue.server.ServerMainWindow;

/**
 * @author xuyue
 *
 */
public class ReceiveThread extends Thread {

	private ServerMainWindow mw;
	private Socket socket;
	private Packet packet;
	public ReceiveThread(Socket socket, ServerMainWindow mw) {
		this.mw = mw;
		this.socket = socket;
	}
	@Override
	public void run() {
		while(true){
				Object obj;
				ObjectInputStream ois ;
				try {
					ois = new ObjectInputStream(socket.getInputStream());
					obj = ois.readObject();
					if(!(obj instanceof Packet)){
						mw.appendMessage("接收packet失败！packet已经损坏，无法解析。");
					}
					packet = (Packet) obj;
					mw.appendMessage("接收到packet：来自" + packet.getSourceIP() + ":"
							+ packet.getSourcePort() + ",序列号为" + packet.getSequenceNumber());
					handlePacket(packet);
				} catch (ClassNotFoundException e) {
					// TODO Auto-generated catch block
					mw.appendMessage("接收packet失败！");
					e.printStackTrace();
				} catch (IOException e) {
					// TODO Auto-generated catch block
					mw.appendMessage("接收packet失败！");
					e.printStackTrace();
					if(e instanceof SocketException || e instanceof EOFException){
						break;
					}
				}
		}
		
	}

	private void handlePacket(Packet p){
		if(p.getSequenceNumber() == mw.getNextExceptSequence()){
			mw.appendMessage("接收到正在等待的packet" + p.getSequenceNumber() + ",准备检验checksum");
			if(p.getChecksum() == p.countChecksum()){
				responseACK(p.getSequenceNumber());
				if(p.getFlag() == 1){
					mw.appendMessage("packet" + p.getSequenceNumber() + "checksum正确，向上层提交数据" + p.getData() + ",回复ACK,等待下一个包");
					mw.setNextExceptSequence(mw.getNextExceptSequence() + 1);
				}else{
					mw.appendMessage("packet" + p.getSequenceNumber() + "checksum正确" + p.getData() + ",回复ACK,本次传输完成。");
				}
				
			}else {
				mw.appendMessage("packet" + p.getSequenceNumber() + "checksum出错，回复上一个ACK,丢弃该包！");
				responseACK(mw.getNextExceptSequence() - 1);
			}
		}else{
			mw.appendMessage("正在等待序列号为" + mw.getNextExceptSequence() + "的packet，但接收到" + p.getSequenceNumber() + ",丢弃该包！回复上一个ACK");
			responseACK(mw.getNextExceptSequence() - 1);
		}
		
	}
	/*
	 * 发送应答的ACK
	 */
	private void responseACK(int num){
		try {
			double prob = Math.random();
			//模拟丢包
			if(prob < C.server.probilityLose){
				mw.appendMessage("ACK" + num + "模拟丢包！");
				return;
			}
			Packet p = new Packet();
			p.setSourceIP(C.server.ipAddress);
			p.setSourcePort(C.server.port);
			p.setDestinationIP(C.client.ipAddress);
			p.setDestinationPort(C.client.port);
			p.setSequenceNumber(num);
			p.setData("ack");
			prob = Math.random();
			//受干扰
			if(prob < C.server.probilityDisturb){
				p.setWrongChecksum();
			}else{
				p.setCorrectChecksum();
			}
			ObjectOutputStream oos = new ObjectOutputStream(socket.getOutputStream());
			oos.writeObject(p);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
