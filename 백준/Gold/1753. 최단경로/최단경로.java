import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	private static int V;
	private static List<int[]>[] graph;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		V = sc.nextInt();
		int E = sc.nextInt();
		int startNode = sc.nextInt();
		graph = new ArrayList[V + 1];

		for (int i = 1; i <= V; i++) {
			graph[i] = new ArrayList<int[]>();
		}

		for (int i = 0; i < E; i++) {
			int start = sc.nextInt();
			int end = sc.nextInt();
			int weight = sc.nextInt();
			graph[start].add(new int[] {end, weight});
		}
		bfs(startNode);
	}

	private static void bfs(int startNode) {
		int[] visited = new int[V + 1];
		Arrays.fill(visited, Integer.MAX_VALUE);
		visited[startNode] = 0;
		Queue<int[]> queue = new PriorityQueue<>((o1, o2) -> o1[1] - o2[1]);
		queue.offer(new int[] {startNode, 0});
		while (!queue.isEmpty()) {
			int[] poll = queue.poll();
			int node = poll[0];
			int dist = poll[1];

			if (dist > visited[node])
				continue;
			for (int[] edge : graph[node]) {
				int nextNode = edge[0];
				int weight = edge[1];
				int newDist = dist + weight;

				if (newDist < visited[nextNode]) {
					visited[nextNode] = newDist;
					queue.offer(new int[] {nextNode, newDist});
				}
			}
		}
		for (int i = 1; i <= V; i++) {
			if (visited[i] == Integer.MAX_VALUE) {
				System.out.println("INF");
			} else {
				System.out.println(visited[i]);
			}
		}
	}
}
