/**
 * 
 */
package com.xuyue.common;

/**
 * @author xuyue
 * 
 */
public class C {
	public static final class server {
		public static final String ipAddress = "127.0.0.1";
		public static final int port = 12222;
		public static final double probilityDisturb = 0.05;
		public static final double probilityLose = 0.1;
	}

	public static final class client {
		public static final String ipAddress = "127.0.0.1";
		public static final int port = 11111;
		public static final double probilityDisturb = 0.1;
		public static final double probilityLose = 0.05;
		public static final int timeDelay = 10000;
		public static long sendInterval = 1000;
	}
}
