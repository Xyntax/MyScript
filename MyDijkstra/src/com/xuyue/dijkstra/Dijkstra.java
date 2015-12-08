package com.xuyue.dijkstra;

import java.util.Random;

import com.xuyue.grap.Grap;

public class Dijkstra {
	public static int min(int[] a) {

		// 返回数组中的最小值的下标
		int min = a[0];
		int minsign = 0;
		for (int i = 0; i < a.length; i++) {
			if (a[i] != 0) {
				if (a[i] < min) {
					min = a[i];
					minsign = i;
				}
			}
		}

		return minsign;

		// min表示最小值，minsign表示对应的元素下标

	}

	public static String[] closestpath(String[] route, String[] p, int star) { // 计算各条最短路径并且保存于字符串数组中
		int num = route.length; // 获取节点数
		int sorce = star;

		// 获取源节点
		String[] vname = route;

		// 获取顶点集
		String[] path = new String[num]; // 路径
		for (int i = 0; i < num; i++)
			path[i] = vname[i] + " ";
		String p1 = "AB";
		for (int i = 0; i < num; i++) {
			if (i != sorce) {
				p1 = p[i];

				// 采用逆推思维，从后向前依次表示

				path[i] += p1 + " ";
				while (p1 != null && (!p1.equals(vname[sorce]))) {
					// 逆推至源节点表示最短路径完全确定了
					for (int t = 0; t < num; t++) {
						if (vname[t].equals(p1))
							p1 = p[t];
					}

					path[i] += p1 + " ";
				}

			}

		}
		String[][] path01 = new String[num][];

		// 以下部分均是路径显示格式的调整与转换
		String[] truepath = new String[num];
		for (int i = 0; i < num; i++)
			truepath[i] = "";
		for (int i = 0; i < num; i++)
			path01[i] = path[i].split(" ");
		for (int i = 0; i < num; i++)
			path01[i][path01[i].length - 1] = route[sorce];
		for (int i = 0; i < num; i++) {
			for (int j = path01[i].length - 1; j >= 0; j--) {
				if (path01[i][j] != null)
					truepath[i] += path01[i][j] + "  ";
			}
		}
		for (int i = 0; i < num; i++) {
			truepath[i] = truepath[i].replaceAll("  ", "→");
			truepath[i] = truepath[i].substring(0, truepath[i].length() - 1);
		}
		return truepath;
	}

	public static void dijkstra(Grap g, String star) {
		// 获取源节点到各节点最小距离的算法
		int vnum = g.getRoute().length; // 获取节点数
		String source = star;
		// 获取源节点
		String[] v = g.getRoute();

		// 获取顶点集
		int[][] dis = g.getDistance();
		// 获取任意两点间距离值（权值）
		int sorce;
		for (sorce = 0; sorce < vnum; sorce++)
			if (v[sorce].equals(source))

				break;

		// 锁定源节点
		int[] D = new int[vnum];

		// 用来表示源节点到目标节点当前的最短距离
		String[] p = new String[vnum];

		// 表示源节点到目标节点当前最短路径上的前一节点
		int[] closest = new int[vnum];

		// 存放最短距离
		for (int i = 0; i < vnum; i++)
			closest[i] = 10000;
		closest[sorce] = 0;
		for (int i = 0; i < vnum; i++) {
			if (i != sorce) {
				D[i] = dis[sorce][i];
				// 初始化dijkstra算法表第一行
				p[i] = source;

			}

		}
		D[sorce] = 10000;
		int sv = 1;

		// 标志当前已经纳入集合的节点个数
		while (sv < vnum) {
			int sign = min(D); // 获取所有距离值中最小的一个的路由器下标
			sv++;

			// 把该节点加入到集合中；
			for (int i = 0; i < vnum; i++) {
				if (i != sorce && D[i] != 9999) {

					// 已经考虑过的节点不再考虑范围内
					if (D[i] > dis[sign][i] + D[sign]) {
						D[i] = dis[sign][i] + D[sign];

						// 更新最小距离的表
						p[i] = v[sign];

						// 更新最短路径的前一个节点
					}
				}
			}
			closest[sign] = D[sign];
			D[sign] = 9999;
		}
		String[] closestpath = closestpath(v, p, sorce);

		// 在获得了最小距离后，立刻求找对应的最短距离

		for (int i = 0; i < vnum; i++) {
			if (i != sorce && closest[i] < 9999) {

				// 显示源节点到各目标节点的最小距离和最短路径
				System.out.print("【计算】路由" + source + "到路由" + v[i] + "的最短距离是"
						+ closest[i]);
				System.out.print("   ");
				System.out.print("最短路径为： " + closestpath[i]);
				System.out.println();
			} else {
				if (!source.equals(v[i])) {

					// 若不可达给予显示
					System.out.print("【计算】路由" + source + "不能到达路由" + v[i]);
					System.out.println();
				}
			}
		}

	}

	public static void main(String[] args) {
		int num = 0;

		while (num == 0)
			num = new Random().nextInt(22);

		// 设定路由器数量的随机值
		String[] route = new String[num];

		// 初始化顶点集
		for (int i = 0; i < num; i++)
			route[i] = i + ""; // 初始化顶点名称
		Grap g = new Grap(route);

		// 初始化图
		int sorce = new Random().nextInt(num);

		// 随机选取源节点
		System.out.println("【随机】选取的源节点是路由" + route[sorce]);
		dijkstra(g, route[sorce]);
		// 运行Dijkstra算法
	}

}