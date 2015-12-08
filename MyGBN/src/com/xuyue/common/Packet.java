/**
 * 
 */
package com.xuyue.common;

import java.io.Serializable;

/**
 * @author xuyue
 *
 */
public class Packet  implements Serializable{
	/**
	 * 
	 */
	private static final long serialVersionUID = -8895085387492502788L;
	private String sourceIP;
	private String destinationIP;
	private int sourcePort;
	private int destinationPort;
	private int sequenceNumber;
	private int checksum;
	private String data;
	private int flag;
	public String getSourceIP() {
		return sourceIP;
	}
	public void setSourceIP(String sourceIP) {
		this.sourceIP = sourceIP;
	}
	public String getDestinationIP() {
		return destinationIP;
	}
	public void setDestinationIP(String destinationIP) {
		this.destinationIP = destinationIP;
	}
	public int getSourcePort() {
		return sourcePort;
	}
	public void setSourcePort(int sourcePort) {
		this.sourcePort = sourcePort;
	}
	public int getDestinationPort() {
		return destinationPort;
	}
	public void setDestinationPort(int destinationPort) {
		this.destinationPort = destinationPort;
	}
	public int getSequenceNumber() {
		return sequenceNumber;
	}
	public void setSequenceNumber(int sequenceNumber) {
		this.sequenceNumber = sequenceNumber;
	}
	public int getChecksum() {
		return checksum;
	}
	public void setChecksum(int checksum) {
		this.checksum = checksum;
	}
	
	/**
	 * º∆À„checksum
	 * @return
	 */
	public int countChecksum(){
		int sum = -1;
		if(data == null){
			return sum;
		}
		for(int i = 0; i < data.length(); ++i){
			sum += data.charAt(i);
		}
		return sum;
	}
	
	public void setCorrectChecksum(){
		this.checksum = countChecksum();
	}
	
	public void setWrongChecksum(){
		this.checksum = -1;
	}
	public String getData() {
		return data;
	}
	public void setData(String data) {
		this.data = data;
	}
	public int getFlag() {
		return flag;
	}
	public void setFlag(int flag) {
		this.flag = flag;
	}
}
