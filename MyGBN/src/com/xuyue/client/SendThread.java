/**
 * 
 */
package com.xuyue.client;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;
import java.net.SocketException;
import java.net.UnknownHostException;
import java.util.ArrayList;
import javax.swing.Timer;
import com.xuyue.client.ClientMainWindow;
import com.xuyue.client.SendThread.SendDataThread;
import com.xuyue.client.SendThread.Timeout;
import com.xuyue.common.C;
import com.xuyue.common.Md5;
import com.xuyue.common.Packet;

/**
 * @author xuyue
 *
 */
public class SendThread extends Thread {
	private ClientMainWindow mw;
	public static final int PACKET_AMOUNT = 15;//要发送的包的总个数
	public String allData[];
	private int nextSendNum = 0;//待发送的下一个数据的序号
	private ArrayList<Packet> sndpkt;
	private int N = 5;//窗口大小
	private int base;//窗口中确认收到无错ACK的包序号最大值
	private int nextSeqNum;//下一个待确认的包的序号
	private Socket socket;	
	private boolean forceStop;	//是否强制停止
	private boolean working;//判断是否停止工作
	private Timer timer;//计时器
	public SendThread(ClientMainWindow mw){
		this.mw = mw;
		initAllData();
		sndpkt = new ArrayList<Packet>();
		boolean exception = false;
		try {
			socket = new Socket(C.server.ipAddress, C.server.port);
		} catch (UnknownHostException e) {
			mw.appendMessage("无法建立网络连接，请退出重试");
			exception = true;
			e.printStackTrace();
		} catch (IOException e) {
			mw.appendMessage("无法建立网络连接，请退出重试");
			exception = true;
			e.printStackTrace();
		}
		if(!exception){
			mw.appendMessage("已经建立网络连接，即将开始模拟GBN");
			new SendDataThread().start();
		}
	}
	/*
	 * 初始化需要发送数据
	 */
	private void initAllData(){
		allData = new String[PACKET_AMOUNT];
		for(int i = 0; i < PACKET_AMOUNT; ++i){
			allData[i] = Md5.md5(Math.random() + "");
			System.out.println("第"+i+"个："+allData[i]);
		}
	}

	public int getNextSendNum() {
		return nextSendNum;
	}

	public void setNextSendNum(int nextSendNum) {
		this.nextSendNum = nextSendNum;
	}
	/*
	 * 
	 */
	private boolean rdtSend(String data){
		if(nextSeqNum < base + N){
			Packet p = makePacket(nextSeqNum, data);
			sndpkt.add(p);
			udtSend(p);
			mw.appendMessage("packet" + p.getSequenceNumber() + "正常发出");
			if(base == nextSendNum){
				startTimer();
			}
			nextSeqNum++;
			return true;
		}else{
			refuseData(data);
			return false;
		}
	}
	
	/**
	 * 打包
	 * @param nextSeqNum
	 * @param data
	 * @return
	 */
	private Packet makePacket(int nextSeqNum, String data){
		Packet p = new Packet();
		p.setData(data);
		p.setSequenceNumber(nextSeqNum);
		p.setSourceIP(C.client.ipAddress);
		p.setSourcePort(C.client.port);
		p.setDestinationIP(C.server.ipAddress);
		p.setDestinationPort(C.server.port);
		p.setCorrectChecksum();
		//当打包最后一个数据块时，将flag置为0
		if(nextSeqNum == PACKET_AMOUNT - 1){
			p.setFlag(0);
			mw.appendMessage("打包最后一个数据块");
		}else{
			p.setFlag(1);
		}
		return p;
	}
	/*
	 * 窗口数已满,拒绝发送数据
	 */
	private void refuseData(String data)
	{
		mw.appendMessage("窗口数已满,拒绝发送数据:" + data);
	}
	/*
	 * 	
	 */
	private void udtSend(Packet p){
		mw.appendMessage("发送packet" + p.getSequenceNumber());
		double prob = Math.random();
		//10%几率丢包,让客户端认为已经发送，实际根本没有发送，必然丢失
		if(prob < 0.1){
			mw.appendMessage("packet" + p.getSequenceNumber() + "模拟丢包");
		}
		prob = Math.random();
		//10%几率收到干扰导致checksum出错
		if(prob < 0.1){
			p.setWrongChecksum();
		}else{
			p.setCorrectChecksum();
		}
		try {
			ObjectOutputStream oos = new ObjectOutputStream(socket.getOutputStream());
			oos.writeObject(p);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
	/*
	 * 判断接收到的ACK包是否被破坏
	 * 被破坏了，返回false
	 * 没有被破坏，返回true
	 */
	private boolean rdtRcv(Packet p)
	{
		if(p != null)
			return true;
		else
			return false;
	}
	/*
	 * 无错ACK到达，判断ackNo是否未完成分组有关，即检查checksum是否正确
	 * ackNo与未完成分组无关，丢弃该ACK
	 * ackNo与未完成分组有关，继续下一步
	 */
	private boolean notCorrupt(Packet p)
	{
		if(p == null){
			return false;
		}
		if(p.getChecksum() == p.countChecksum()){
			mw.appendMessage("接收到ack" + p.getSequenceNumber() + "且checksum正确");
		}else{
			mw.appendMessage("接收到ack" + p.getSequenceNumber() + "但checksum错误");
		}
		return true;
	}
	
	private void startTimer(){
		if(timer != null){
			timer.stop();
		}
		timer = new Timer(C.client.timeDelay, new Timeout());
		timer.start();
		mw.appendMessage("开始计时器");
	}
	/*
	 * 停止计时
	 */
	private void stopTimer(){
		if(timer != null){
			timer.stop();
		}
		mw.appendMessage("停止计时");
	}
	/*
	 * 强制停止socket
	 */
	public void forceStop(){
		forceStop = true;
		if(socket != null){
			try {
				socket.close();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		timer.stop();
	}
	@Override
	public void run() {
		while(!forceStop){
			Packet p = null;
			try {
				ObjectInputStream ois = new ObjectInputStream(socket.getInputStream());
				Object obj = ois.readObject();
				if(obj instanceof Packet){
					p = (Packet) obj;
					System.out.println("收取ack");
					if(!rdtRcv(p)){
						mw.appendMessage("接收到一个损坏的packet，丢弃！");
					}
					if(notCorrupt(p) && p.getSequenceNumber() >= base){
						if(p.getSequenceNumber() == PACKET_AMOUNT - 1){
							working = false;
							mw.appendMessage("接收到最后一个包的ACK！完成传输。");
							stopTimer();
						}
						base = p.getSequenceNumber() + 1;
						if(base == nextSeqNum){
							stopTimer();
						}else{
							startTimer();
							mw.appendMessage("重启计时器");
						}
					}
				}
				
			} catch (ClassNotFoundException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
				if(e instanceof SocketException){
					break;
				}
			}
		}
	}
	/*
	 * 超时处理
	 */
	class Timeout implements ActionListener {
		
		public void actionPerformed(ActionEvent e){//在计时器超时的情况下
			startTimer();
			mw.appendMessage("超时，从" + base + "重发");
			for(int i = base;i < nextSeqNum; ++i)
			{
				udtSend(sndpkt.get(i));
			}
		}
	}
	/*
	 * 发送数据
	 */
	class SendDataThread extends Thread{

		@Override
		public void run() {
			while(nextSeqNum < PACKET_AMOUNT || working){
				if(forceStop){
					break;
				}
				if(rdtSend(allData[nextSendNum])){
					nextSendNum++;
				}
				try {
					Thread.sleep(C.client.sendInterval);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
		}
		
	}
}
