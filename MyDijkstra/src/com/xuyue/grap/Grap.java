package com.xuyue.grap;

import java.util.Random;

public class Grap {
	private String[] route;
	private int[][] distance;
	private int count = 0;

	public Grap(String[] v) {
		route = v;
		// 获取顶点集
		distance = new int[route.length][route.length];
		// 用二维数组保存任意两条边的距离
		System.out.print("【随机】设置了" + v.length + "个路由器  "); // 统计路由器总数
		System.out.print("路由名分别为：  ");
		for (int i = 0; i < v.length; i++)
		{
			System.out.print(v[i]);
			System.out.print("  ");// 依次显示路径名称
		}
		System.out.println();
		// 设置自己到自己的距离为0
		for (int i = 0; i < route.length; i++)
		{
			distance[i][i] = 0;
		}	
		for (int i = 0; i < route.length - 1; i++) 
		{
			System.out.print("【随机】路由" + route[i] + "到其他路由的距离依次为： ");
			for (int j = i + 1; j < route.length; j++) {
				int ran = new Random().nextInt(150);
				// 设定随机值
				if (ran > 100) 
				{
					// 设置一定的概率出现“无穷大”
					distance[i][j] = 10000;
					System.out.print("   ∞");
					distance[j][i] = distance[i][j];
				} 
				else
				{
					distance[i][j] = ran;
					System.out.print("   ");
					System.out.print(ran);
					// 依次显示每个顶点到其他顶点的距离
					distance[j][i] = ran;
					count++;
				}
			}
			System.out.println();
		}
		System.out.print("【统计】本架构中总共有：  ");
		// 统计有限权值边的条数
		System.out.print(count);
		System.out.print("  条边！");
	}

	public String[] getRoute() {
		return route;
	}

	public void setRoute(String[] route) {
		this.route = route;
	}

	public int[][] getDistance() {
		return distance;
	}

	public void setDistance(int[][] distance) {
		this.distance = distance;
	}

	public int getCount() {
		return count;
	}

	public void setCount(int count) {
		this.count = count;
	}
	
}
