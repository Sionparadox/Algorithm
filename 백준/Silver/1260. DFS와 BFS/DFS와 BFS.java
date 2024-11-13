import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	private static boolean[] visited;
	private static ArrayList<ArrayList<Integer>> gragh = new ArrayList<>();

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int V = sc.nextInt();
		visited = new boolean[N + 1];
		for (int i = 0; i <= N; i++) {
			gragh.add(new ArrayList<>());
		}

		for (int i = 1; i <= M; i++) {
			int x = sc.nextInt();
			int y = sc.nextInt();
			gragh.get(x).add(y);
			gragh.get(y).add(x);
		}

		for (int i = 1; i <= N; i++) {
			gragh.get(i).sort(Integer::compareTo);
		}
		dfs(V);
		System.out.println();
		Arrays.fill(visited, false);
		bfs(V);
	}

	private static void dfs(int start) {
		visited[start] = true;
		System.out.print(start + " ");
		for (var x : gragh.get(start)) {
			if (!visited[x]) {
				dfs(x);
			}
		}
	}

	private static void bfs(int start) {
		visited[start] = true;
		System.out.print(start + " ");
		Queue<Integer> queue = new LinkedList<>();
		queue.offer(start);
		while (!queue.isEmpty()) {
			for (int node : gragh.get(queue.poll())) {
				if (!visited[node]) {
					queue.offer(node);
					visited[node] = true;
					System.out.print(node + " ");
				}
			}
		}
		System.out.println();
	}
}
